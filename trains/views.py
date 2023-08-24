import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views import View

from trains.models import Train
from users.models import Config
from words.models import Word
from django.db.models import Count


# Create your views here.
class TrainsIndex(LoginRequiredMixin, View):
    #     LoginRequiredMixin 로그인 되어 있는지 확인하고 안되어 있으면 러그린 화면으로 가는 class
    login_url = 'login'  # 로그인 페이지 URL 설정

    def get(self, request):
        user = request.user
        try:
            config = Config.objects.get(id_user=user.id)
        except ObjectDoesNotExist:
            config = Config()
        context = {'config': config}
        return render(request, 'trains/trains_setting.html', context)

    def post(self, request):
        user = request.user

        train_word_count = request.POST.get('train_word_count')
        train_repeat = request.POST.get('train_repeat')
        TrainsUtil.train_repeat = max(1, int(train_repeat))  # max() 함수를 사용하여 두 값 중에서 더 큰 값을 선택
        train_seconds = request.POST.get('train_seconds')
        train_tts_play = request.POST.get('train_tts_play')
        config_data_dict = {
            'train_word_count': train_word_count,
            'train_repeat': TrainsUtil.train_repeat,
            'train_seconds': train_seconds,
            'train_tts_play': train_tts_play,
        }
        try:
            config = Config.objects.get(id_user=user.id)
            TrainsUtil.config_save(config, config_data_dict)
        except ObjectDoesNotExist:
            config = Config()
            config.id_user = user
            TrainsUtil.config_save(config, config_data_dict)

        train_count = int(train_word_count)
        all_words = Word.objects.all()
        TrainsUtil.train_word_list = random.sample(list(all_words), train_count)  # 중복 없는 랜덤 Word 리스트 생성
        train_word_dict = TrainsUtil.get_train_word_dict(TrainsUtil.train_word_list[0])

        context = {'train_word': train_word_dict, 'show_num': 1, 'train_repeat': TrainsUtil.train_repeat}
        return render(request, 'trains/trains_show.html', context)


class TrainsShow(LoginRequiredMixin, View):
    login_url = 'login'  # 로그인 페이지 URL 설정

    def get(self, request):
        return TrainsUtil.get_system_message_render(request, "페이지 접근 오류 ", 'trains-setting')

    def post(self, request):
        show_num = int(request.POST.get('show_num'))

        train_en_word = request.POST.get('train_en_word')
        user = request.user
        word = Word.objects.get(en_word=train_en_word)

        try:
            train = Train.objects.get(id_user=user.id, id_word=word.id)
            train.train_count += 1
            train.save()
        except ObjectDoesNotExist:
            train = Train()
            train.train_count = 1
            train.id_user = user
            train.id_word = word
            train.save()

        if show_num < len(TrainsUtil.train_word_list):
            train_word_dict = TrainsUtil.get_train_word_dict(TrainsUtil.train_word_list[show_num])
            context = {'train_word': train_word_dict, 'show_num': show_num + 1,
                       'train_repeat': TrainsUtil.train_repeat}
            return render(request, 'trains/trains_show.html', context)

        else:
            TrainsUtil.train_repeat -= 1
            if TrainsUtil.train_repeat == 0:
                return redirect('word-practice-history')
            else:
                train_word_dict = TrainsUtil.get_train_word_dict(TrainsUtil.train_word_list[0])
                context = {'train_word': train_word_dict, 'show_num': 1, 'train_repeat': TrainsUtil.train_repeat}
                return render(request, 'trains/trains_show.html', context)


class WordPracticeHistory(View):
    def get(self, request):
        user = request.user

        recent_practice_words = Train.objects.filter(id_user=user).order_by('-update_date')[:10]
        frequent_practice_words = Train.objects.filter(id_user=user).values('id_word__en_word', 'id_word__ko_word_1').annotate(total_practice=Count('id_word__ko_word_1')).order_by('-total_practice')[:10]

        context = {
            'recent_practice_words': recent_practice_words,
            'frequent_practice_words': frequent_practice_words,
        }

        return render(request, 'trains/word_practice_history.html', context)


class TrainsUtil:
    # 연습 단어 리스트를 단어 시작할 때 저장하고 연습이 끝나면 초기화
    train_word_list = []
    train_repeat = 0

    @staticmethod
    def config_save(config: Config, config_data_dict):
        config.train_word_count = config_data_dict['train_word_count']
        config.train_repeat = config_data_dict['train_repeat']
        config.train_seconds = config_data_dict['train_seconds']
        config.train_tts_play = config_data_dict['train_tts_play']
        config.save()

    @staticmethod
    def get_en_phonetics(en_phonetics):
        if ',' in en_phonetics:
            phonetics = en_phonetics.strip().split(',')
            make_phonetics = f"미국식:[{phonetics[0]}],  영국식:[{phonetics[1]}]"
        else:
            make_phonetics = f"미국식:[{en_phonetics}],  영국식:[{en_phonetics}]"
        return make_phonetics

    @staticmethod
    def get_train_word_dict(train_word):
        train_word_dict = model_to_dict(train_word)
        train_word_dict['en_phonetic'] = TrainsUtil.get_en_phonetics(train_word_dict['en_phonetic'])
        train_word_dict['word_class'] = f"{{{train_word_dict['word_class']}}}"
        train_word_dict['ko_phonetic'] = f"({train_word_dict['ko_phonetic']})"
        train_word_dict['ko_romanize'] = f"[{train_word_dict['ko_romanize']}]"

        if ',' in train_word_dict['ko_word_2']:
            train_word_dict['ko_word_2'] = train_word_dict['ko_word_2'].replace(',', ', ')
        return train_word_dict

    @staticmethod
    def get_system_message_render(request, error_message, set_urls):
        context = {'system_message': error_message, 'set_urls': set_urls}
        return render(request, 'system_message.html', context)
