# Django 명령어 사용법


## 패키지 설치

- Django version 5.0.3
- [https://pypi.org/project/django/](https://pypi.org/project/django/)

```
$ pip install django==5.0.3
```

## 프로젝트 생성

- 프로젝트 폴더 생성
- 프로젝트 폴더 내에서 다음 명령어 실행
- 마지막 . 빼먹지 마세요

```
$ mkdir hello-project
$ cd hello-project 
$
$ django-admin startproject django_project . 
```


## manage.py 명령어

- 앱( 서비스 ) 생성
    - api 
    - cms
    - ...

```
$ python manage.py startapp <앱이름>
```

- 개발 서버 실행

```
$ python manage.py runserver
$ python manage.py runserver 127.0.0.1:8000
$ python manage.py runserver 10.0.10.100:8000
$ python manage.py runserver 10.0.10.100:8000 --settings=django_project.settings
```

- 데이터 베이스 관련

```
$ python manage.py makemigrations
$ python manage.py migrate
```

- 관리자 계정 생성

```
$ python manage.py createsuperuser
```

