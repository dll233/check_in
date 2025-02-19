'''
SERVERCHAN 通知
'''

import requests

import time
import hmac
import hashlib
import base64
import urllib.parse

class Serverchan(object):
    def __init__(self, token):
        self.token = token

    def push(self, title, msg):
        print(f'检测到 "SERVERCHAN" 准备推送: {msg}')

        url = 'https://sctapi.ftqq.com/{}.send'.format(self.token)
        #url = 'https://api2.pushdeer.com/message/push?pushkey={}'.format(self.token)
        #url = 'https://api2.pushdeer.com/message/push?pushkey={}&text='.format(self.token)
        #url = 'https://api2.pushdeer.com/{}.send'.format(self.token)
        #print(url)

        session = requests.Session()

        data = {'text':msg,'desp':msg}
        response = session.post(url, data = data)
        # print(url)
        # print(response)
        # print(response.json())
        return response
