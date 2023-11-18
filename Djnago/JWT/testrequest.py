# pip install requests
import requests

HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

# 사용자가 본 html파일에 입력 form에서 입력한 데이터라고 생각해주세요. 
LOGIN_INFO = {
    "email": "hojun@gmail.com",
    "password": "dlghwns1234!"
}

# 로그인을 위해 post요청을 보냅니다.
response = requests.post(LOGIN_URL, data=LOGIN_INFO)
print(response.status_code)
print(response.text)
print(response.json()['access_token'])

token = response.json()

