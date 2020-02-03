import requests
import time
from datetime import datetime


class utvAPP:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            # 登录需要使用这个Referer
            'Referer': 'http://campaign.utvhk.com/jfdk/index.html'
        }

    def utv(self, username, userid):
      	 self.phoneNum = username
      	 self.phoneId = userid
    	 login_url = 'http://campaign.utvhk.com/jfdk/login.do'
    	 login_data = {
    	     "deviceID": "8e6aab4ec4c41e16d2933474169e8a1e",
    	     "isBuySpecialProductPackage": [],
    	     "isCMHKUser": "true",
    	     "lastLoginTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
    	     
    	     "nickName": "52****76",
    	     "registeTime": "2020-02-02T18:51:13",
    	     "userID": self.phoneId,
    	     "userPhone": self.phoneNum,
    	     "watchTime": []
    	  }
        login_req = self.session.post(login_url, data=login_data, headers=self.headers)
        login_msg = '登录情况：' + login_req.json()['msg'] + '\n'
        return login_msg
