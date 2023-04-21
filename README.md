# GameNara
* 자바스크립트를 이용한 간단한 게임사이트 제작  

***

# 개발환경
* VisualStudioCode
* Python 3.9.13 
* Django 4.1  

# 프로젝트
프로젝트 개발기간: 2023/12/30 ~ 2023/01/09  
프로젝트 구성원: 이상엽, 은경찬, 이한결  


# 실행  
1.아나콘다(anaconda3) 설치  
2.비주얼 스튜디오 설치  
3.아나콘다 프롬프트 실행후 장고(django)설치  
```  
conda install django
```
4.프로젝트 경로에서 다음의 코드 실행  
```
python manage.py runserver
```
5.브라우저 주소창에 127.0.0.1:8000/ 입력후 접속

# 설명
1.BallMung(볼멍)

2.PuzzleGame
* 사용자가 원하는 이미지로 무작위로 배치된 타일을 원래의 이미지의 형태로 만드는 퍼즐게임

3.ShootingGame

공통사항
게임내 기록을 DB에 저장해 순위표에 나오게함
