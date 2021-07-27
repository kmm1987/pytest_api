'''
Code description：获取token
Create time：2020-12-03
Developer：叶修
ado:获取登录token
'''
import os
import urllib3
from common.http_requests1 import HttpRequests
from common.logger import Log
from common.read_save_data import Read_Save_Date


class Get_Token(object):

    def get_token(self,account='380024560@qq.com',password='Bb000000'):
        #url = "http://192.168.2.199:9092/v1/auth/developer/accountLogin"
        #url = os.environ["host"]+"/v1/auth/developer/accountLogin"
        url = os.environ["host"]+"/rest/getToken"
        #url = "https://portal.summer-ospp.ac.cn/summer/rest/getToken"
        headers = {"Content_Type":"x-www-form-urlencoded"} #7.11日增加
        body = {
            "username": account,
            "password": password
        }
        urllib3.disable_warnings()
        #r = HttpRequests().post(url, json=body,verify=False)
        r = HttpRequests().get(url,params=body,headers=headers,verify=False)
        #print(r.text)
        #print(r.json())
        #token = r.json()['data']['token']
        token = r.json()["data"]["token"]
        # params = {
        #     "access_token": token
        #     #"token":token
        # }
        Read_Save_Date().save_file('D:\pytest+requests+allure\data\save_data\get_token.txt',token)
        try:
            token!=None
            header_key = {"Token":token}
            HttpRequests().headers.update(header_key)#更新token到header
            print(HttpRequests().headers.update(header_key))
        except Exception as e:
            Log().info("获取不到token:{}".format(e))
        #print(HttpRequests().headers.get("Token",token))
        # print(HttpRequests().headers.update(header_key))
        return token

if __name__ == '__main__':
    print(Get_Token().get_token())
