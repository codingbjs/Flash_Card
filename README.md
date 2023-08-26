# Flash Card 프로젝트 개요

## 프로젝트 개요
- 프로젝트 명: Flash-Card 웹 어플리케이션
- 프로젝트 기간: 2023년 8월 22일 ~ 2023년 8월 25일
- 프로젝트 팀: Python Team 5 (홍태광, 정동우, 장우림, 이진수, 원용석)

Flash Card 프로젝트는 사용자가 단어를 효과적으로 관리하고 학습하는데 도움을 주는 웹 어플리케이션입니다.

단어 데이터 입력, 단어 연습, 단어 테스트 기능을 통해 사용자의 언어 학습을 지원합니다.

## 주요 목표
1. 단어 관리의 용이성: 사용자는 웹 어플리케이션을 통해 단어와 그에 대한 정보를 간편하게 입력하고 관리할 수 있습니다.
2. 효율적인 학습 지원: 입력한 단어를 기반으로 연습 세트를 생성하여 사용자에게 학습 기회를 제공하며, 다양한 유형의 테스트를 통해 학습 효율을 높입니다.
3. 학습 결과 기록 및 분석: 사용자의 학습 이력과 성적을 기록하여 개인의 학습 경과를 분석하고 개선 방향을 제시합니다.

## 기능 설명

### 1. 단어 데이터 입력 기능
- 사용자는 웹 어플리케이션을 통해 단어와 그에 대한 정보(의미, 발음 등)를 입력할 수 있습니다.
- 단어에 대한 정보는 웹크롤링 기술을 활용하여 자동으로 수집됩니다. 
- 입력한 단어 데이터는 데이터베이스에 저장되어 나중에 활용됩니다.

### 2. 단어 연습 기능
- 사용자가 입력한 단어 데이터를 기반으로 연습 세트를 생성합니다.
- 사용자는 연습 세트의 어려움 난이도와 연습 횟수를 설정하여 학습합니다.
- 연습 결과와 성적은 기록되어 나중에 확인할 수 있습니다.

### 3. 단어 테스트 기능
- 사용자에게 단어를 보여주고 해당 단어의 의미나 발음을 입력하는 테스트를 제공합니다.
- 다양한 난이도와 유형의 테스트를 통해 사용자의 단어 이해도와 기억력을 측정합니다.
- 테스트 결과와 점수는 기록되어 나중에 테스트 이력을 확인할 수 있습니다.

## 기대 효과
- 사용자는 편리한 단어 입력과 관리를 통해 학습 효율이 향상됩니다.
- 단어 연습과 테스트를 통해 사용자의 단어 이해도와 기억력을 강화시킬 수 있습니다.
- 사용자의 학습 이력을 분석하여 맞춤 학습 전략을 제시합니다.

## 개발 환경 및 기술 스택
- 프론트엔드: HTML, CSS, JavaScript, Bootstrap
- 백엔드: Django (Python) - BeautifulSoup, requests, gTTS
- 데이터베이스: SQLite

## 개발 일정
- 요구 사항 분석 및 기획: 1일 - 
- 데이터베이스 설계 및 구축: 1일
- 기능 개발 및 테스트: 3일
- 디자인 및 UI/UX 개선: 1일
- 배포 및 최종 테스트: 1일

## 향후 계획
- 단어 데이터 관리 기능 강화: 동의어, 반의어 등 다양한 정보 입력 지원
- AI 기능 추가: 사용자 학습 패턴 분석 및 맞춤 학습 추천
- 모바일 앱 개발: 모바일 환경에서도 학습 가능한 앱 제작