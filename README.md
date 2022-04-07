# NOLLE (Android)

## 프로젝트 개요

---

- NOLLE는 Notifiy only likes, Let’s enjoy로 좋아하는걸 알리고 같이 나누자라는 의미입니다.
- 창의학기제 과목으로 진행한 딥러닝 기반 개인화 맛집 추천 서비스입니다.
- 사용자가 업로드 한 음식점 리뷰에 대한 이미지 및 텍스트, 검색 기록 등을 딥러닝으로 분석하여 성향을 추출 후 나와 유사도가 높은 다른 사용자가 갔던 음식점을 추천해줍니다.
- Yolov3 모델의 경우 [](https://www.notion.so/9ed93986cbf34d53b45ae4d624b36513)총 42가지의 한식, 일식, 중식, 양식 음식에 대한 분류가 가능하며 객체인식 모델 정확성 평가의 경우 TOP-1 정확도 88.61%, TOP-5 정확도 90.13%를 보여주었습니다.
- BiLSTM을 이용하여 구현한 감성분석 모델의 경우 음식에 대한 표현과 장소에 대한 분위기를 범주에 나눠 총 14가지의 텍스트 분류가 가능하며 F1-Score은 90.93%, Accuracy는 90.99%를 보여주었습니다.
- 프로젝트에 사용된 딥러닝 기술에 대한 저널 논문`(개인 성향 추출을 위한 딥러닝 기반 SNS 리뷰 분석 방법에 관한 연구)`을 작성하였습니다.

## 프로젝트 사용 기술 및 라이브러리

---

### ✔ Languauge

- Java, Python

### ✔ Server

- Django

### ✔ Client

- Android

### ✔ 협업

- GitHub

### ✔ Deep-Learning

- Yolov3 (Tensorflow)
- BiLSTM (Tensorflow)

### ✔ Data Base

- MySQL

### ✔ Open API

- Naver Blog Search API
- Google Maps API

### ✔ Library

- Retrofit2

## 주요 기능

---

- 딥러닝 기반 성향 분석 및 성향 기반 추천
- 텍스트, 음성, 이미지로 다양하고 간편한 검색 및 추천 요청
- 실시간 리뷰, 인기 리뷰 및 태그를 통한 추천
- 사용자가 가고 싶은 장소를 PICK해 저장
- SNS의 순기능인 팔로우, 팔로잉, 좋아요 및 포스팅 기능

## 나의 역할

---

- Django api server 개발
- 딥러닝 모델 구현을 위한 데이터 수집 및 증폭, 정제
- 딥러닝 학습을 통한 image detection(yolo3 기반) 모델 구현
- DB 설계
- 추천 모듈 구현

[프로젝트 소개](https://foamy-kookaburra-ef9.notion.site/NOLLE-72324bc1c4534a3d865552af0ceb531f)

