# Django_Chatbot
## AboutME
입력한 조건에 맞게 자기소개서를 작성해주는 서비스입니다

## 목차
[1. 목표와 기능](#1-목표와-기능)<br>
[2. 개발 기술 및 환경](#2-개발-기술-및-환경)<br>
[3. 요구사항 명세와 기능 명세](#3-요구사항-명세와-기능-명세)<br>
[4. 프로젝트 구조와 개발 일정](#4-프로젝트-구조와-개발-일정)<br>
[5. 데이터베이스 모델링(ERD)](#5-데이터베이스-모델링erd)<br>
[6.UI](#6-ui)<br>
[7. 기능](#7-기능)<br>
[8. 개발하며 느낀 점](#8-개발하며-느낀-점)<br>

## 1. 목표와 기능
 ### 1-1. 목표
 - 사용자가 입력한 조건에 맞게 자기소개서를 작성해주는 서비스
 ### 1-2. 기능
 - 회원가입, 로그인, 로그아웃
 - ChatGPT를 이용한 자기소개서 작성
 - ChatGPT와의 채팅

## 2. 개발 기술 및 환경
 ### 2-1. 개발 기술

[FE]
<div>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"> 
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> 
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> 
</div>

[BE]
 <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> 
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
</div>

 ### 2-2. 개발 환경
 <div>
    <img src="https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white"> 
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

## 3. 요구사항 명세와 기능 명세
### 3.1 기본 요구사항
- DRF를 이용하여 구현
- 로그인, 회원가입 기능 구현
- 기본적인 CRUD
- ChatGPT로 요청 보내주는 API를 Django 내에 구현
- 챗봇 API는 로그인을 한 유저만 사용가능
- 각 user 당 하루 5번만 요청 가능
- 저장된 채팅 내역 본인만 조회 가능
- AWS 배포
- URL 연결

### 3.2 권장 요구사항
- 개인 도메인 등록, 프론트엔드, 백엔드 배포
- kakao, github 등 OAuth2 연결


## 4. 프로젝트 구조와 개발 일정
 ### 4-1. 프로젝트 구조

 ```
 📦Django_Chatbot_BE
 ┣ 📂AboutMe
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┃ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂chat
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂venv
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
 ```
```
 📦Django_Chatbot_FE
 ┣ 📂css
 ┃ ┣ 📜accounts.css
 ┃ ┣ 📜chat.css
 ┃ ┗ 📜common.css
 ┣ 📜chat.html
 ┣ 📜login.html
 ┣ 📜signup.html
 ┗ 📜README.md
 ``````

 ### 4-2. URL 구조

|App       |URL                |Method    | 설명      |
|:---------|:------------------|:---------|:----------|
|accounts  |'accounts/login/'  |POST      |로그인     |
|accounts  |'accounts/signup/' |POST      |회원가입   |
|chat      |'chat/'            |POST      |채팅       |

 
 ### 4-3. 개발 일정(WBS)

```mermaid
gantt
    title Django_Chatbot
    dateFormat  YYYY-MM-DD
    section 기획 및 문서작업
    주제 선정 및 기획 :a1, 2023-11-21 , 3d
    UI 설계/목업페이지 작성     :after a1  , 1d
    READEME 작성 : 2023-11-30 , 1d
    section BE
    로그인/회원가입 구현 :a2, 2023-11-24  , 3d
    ChatGPT 연결, 챗봇 구현  :after a2 , 3d
    section FE 
    HTML/CSS 페이지 구현 :a3, 2023-11-26 , 2d
    JS 작성 : 2023-11-27 , 3d
```

## 5. 데이터베이스 모델링(ERD)

<img src="" width="80%">

## 6. UI
### 6-1. 목업페이지
| | |
|:-:|:-:|
|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/a43a3f2e-fdec-4ff3-8fcd-f20375809650" width="100%">메인페이지|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/6deea09f-982f-48de-b270-7a47bd562cad" width="100%">로그인|
|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/07ac5220-bc58-4160-bea4-c4e216a17546" width="100%">회원가입|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/1c0ff820-8869-4779-bba2-f7d3c75daffb" width="100%">양식입력|
|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/2d096b6f-c006-4b1b-b133-e5c24f7cdb1a" width="100%">생성결과|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/476ea073-c74b-4bed-828b-2da619e7dc35" width="100%">채팅창|
|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/000c4552-cf5e-46fa-97d5-0a0d943db01f" width="100%">보관함|<img src="https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/81052a1d-fc52-4f11-9c41-3d381e1a4bfe" width="100%"> 글 상세보기|

## 7. 기능

| | |
|:-:|:-:|
|![gif](https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/3217d88e-fefb-43b1-861e-6e42f822e8c8)|설명|
|![gif](https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/06b06c25-c0fe-4fe0-b6fa-f08bd2e6c34e)|설명|
|![gif](https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/5387464a-3fb2-4f0d-b653-1a296977360b)|설명|
|![gif](https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/e1c22734-9600-460b-8d29-7387425ff36e)|설명|
|![gif](https://github.com/hantang820/Django_Chatbot_BE/assets/142385695/2a96d05c-7db1-4735-81c7-64a1779042be)|설명|


## 8. 개발하며 느낀 점 
- Django를 사용해서 페이지를 개발하는 게 얼마나 편리한지 느낄 수 있었습니다. 또, 모르는 부분이 많아 그 편리함을 제대로 이용하지 못한다는 것이 답답하게 느껴질 때도 많았습니다. 좋은 기능을 잘 활용하기 위해서 더 많이 공부해야겠다는 생각을 하게 된 프로젝트였습니다. 