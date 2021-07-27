'''
Code description:服务相关接口
Create time: 2021/07/11
Developer: lemon
add:需要测试的一类接口
'''
import os
from common.http_requests1 import HttpRequests


class Api_Auth_Service(object):

    def __init__(self):
        self.headers = HttpRequests().headers
        #self.noheaders= HttpRequests().notoken_headers

    def api_home_service_list(self,pageNum='1',pageSize='10',activityId='1'):
        # 活动主页服务列表
        # url = "http://192.168.2.199:9092/v1/auth/auth_service/findAuthService"
        url = os.environ["host"] + "/rest2/applyforproject"  # 读取conftest.py文件地址进行拼接
        payload ={
            "pageNum": pageNum,
            "pageSize": pageSize,
            "activityId": activityId
        }
        headers = {'Content-Type':'x-www-form-urlencoded'}
        response = HttpRequests().get(url, headers=headers, params=payload,verify=False)
        print(response.text)
        # print(response.json())
        return response


    def api_activity_list(self,pageNum='1',pageSize='10'):
        #活动服务列表
        url = os.environ["host"] +"/rest/activityList"
        payload ={
            #"pageNum": "1",
            "pageNum": pageNum,
            #"pageSize": "10",
            "pageSize": pageSize
        }
        response_activi = HttpRequests().get(url, headers=self.headers, params=payload,verify=False)
        print(response_activi.text)
        return response_activi

    def api_program_list(self,pageNum='1',pageSize='10',activityId='1'):
        #项目服务列表
        url = os.environ["host"] +"/rest/programList"
        payload ={
            "pageNum": pageNum,
            "pageSize": pageSize,
            "activityId": activityId
        }
        response_program = HttpRequests().get(url, headers=self.headers, params=payload,verify=False)
        print(response_program.text)
        return response_program

    def api_activityandprogram_list(self,pageNum='1',pageSize='10',activityId='1'):
        #活动和项目服务列表
        url = os.environ["host"] +"/rest/activityAndProgramList"
        payload ={
            "pageNum": pageNum,
            "pageSize": pageSize,
            "activityId": activityId
        }
        response_ap = HttpRequests().get(url, headers=self.headers, params=payload,verify=False)
        print(response_ap.text)
        return response_ap



    # def get_service_id(self):
    #     #获取银行卡三要素认证服务id
    #     url = "http://192.168.2.199:9092/v1/auth/auth_service/findAuthService"
    #     #url = os.environ["host"] + "/v1/auth/auth_service/findAuthService"  # 读取conftest.py文件地址进行拼接
    #     response = HttpRequests().get(url,headers=self.headers)
    #     #print(response.json()['data'][0]['service_list'][0]['id'])
    #     service_id = response.json()['data'][0]['service_list'][1]['id']
    #     return service_id
    #
    # def api_service_info(self,serviceId='0b6cf45bec757afa7ee7209d30012ce1',developerId=''):
    #     #服务详情
    #     body = {
    #         "serviceId" :serviceId,
    #         "developerId":developerId
    #     }
    #     url = "http://192.168.2.199:9092/v1/auth/auth_service/findServiceDetail"
    #     #url = os.environ["host"] + "/v1/auth/auth_service/findServiceDetail"#读取conftest.py文件地址进行拼接
    #     response = HttpRequests().get(url,headers=self.headers,params = body,verify=False)
    #     #print(response.json())
    #     return response
    #
    # def api_add_or_update_service(self,api_param_req,api_param_res,description,error_code,icon,id,interface_remarks,
    #                           name,product_info,request_method,sample_code,sort,type,url):
    #     #服务添加或者更新
    #     body={
    #             "api_param_req": api_param_req,
    #             "api_param_res": api_param_res,
    #             "description": description,
    #             "error_code": error_code,
    #             "icon": icon,
    #             "id": id,
    #             "interface_remarks": interface_remarks,
    #             "name": name,
    #             "product_info": product_info,
    #             "request_method": request_method,
    #             "sample_code": sample_code,
    #             "sort": sort,
    #             "type": type,
    #             "url": url,
    #     }
    #     #url = "http://192.168.2.199:9092/v1/auth/auth_service/insertOrUpdateService"
    #     url = os.environ["host"] + "/v1/auth/auth_service/insertOrUpdateService"  # 读取conftest.py文件地址进行拼接
    #     response = HttpRequests().post(url,json=body,headers=self.headers,verify=False)
    #     return response
    #
    # def api_add_service_price(self,id,max_number,money,service_id,small_number):
    #     #服务价格添加
    #     body = {
    #         "id": id,
    #         "max_number": max_number,
    #         "money": money,
    #         "service_id": service_id,
    #         "small_number": small_number
    #     }
    #     # url = "http://192.168.2.199:9092/v1/auth/auth_service/insertServicePrice"
    #     url = os.environ["host"] + "/v1/auth/auth_service/insertServicePrice"  # 读取conftest.py文件地址进行拼接
    #     response = HttpRequests().post(url, json=body, headers=self.headers, verify=False)
    #     return response
    #
    # def api_apply_service(self,developer_id,service_id):
    #     #申请服务
    #     body ={
    #         "developer_id": developer_id,
    #         "service_id": service_id
    #     }
    #     # url = "http://192.168.2.199:9092/v1/auth/auth_service/applyService"
    #     url = os.environ["host"] + "/v1/auth/auth_service/applyService"  # 读取conftest.py文件地址进行拼接
    #     response = HttpRequests().post(url, json=body, headers=self.headers, verify=False)
    #     return response


if __name__ == '__main__':
    #Auth_Service().api_home_service_list()
    Api_Auth_Service().get_service_id()
    #Auth_Service().api_service_info()