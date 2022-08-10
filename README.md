나볼라고 정리해놓는 문서😙

### git clone
```
git clone https://github.com/o-ddong/DjangoCheckAPI.git
```
### 가상환경 생성
```
python3 -m venv venv
```

### 가상환경 접속
```
source /venv/bin/activate
```

### requestments 설치
request 파일 경로가 있는 곳에서 다음과 같이 실행해주면 된다.
```
pip install -r requestments
```

### requestments
```
Django==2.2.28
djangorestframework==3.12.4
mysqlclient==2.1.1
pkg-resources==0.0.0
pytz==2022.1
sqlparse==0.4.2
```

### Database

📃 settings.py 에서 설정해야됨

### 서버 실행
```
python3 manage.py runserver 0.0.0.0:8000
```

---

### API docs.
<a href=https://graceful-wolverine-41d.notion.site/Check_API-7742b3c61b4a4d819666dc73929a2e20>Check API docs.</a>

### Blog
<a href=https://velog.io/@odh0112/Django-Ubuntu-check-API>Check API Blog.</a>
