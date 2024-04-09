# pip 명령어 사용법

- 파이썬의 패키지 관리자인 pip 사용법 정리
- pip search 동작 하지 않음, 직접 검색 필요함
- [패키지 검색](https://pypi.org/)


## 사전준비

프로젝트별로 파이썬 가상환경 구성을 꼭 먼저 할 것

- Ubuntu-22.04

```
$ sudo apt install python3.10-venv
$ python -m venv .venv-local
$ source .venv-local/bin/activate
```

- Windows

```
$ python -m venv .venv-local
$ .venv-local/Scripts/Activate.ps1
```

## 버전확인

```
$ python --version
$ pip --version
```

## 패키지 설치

```
$ pip install django
$ pip install django==5.0.3
```

```
$ pip install --upgrade django
```

```
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

## 패키지 삭제

```
$ pip uninstall django
```

## 패키지 목록 보기

```
$ pip list
```

## 패키지 정보 학인

```
$ pip show django
```