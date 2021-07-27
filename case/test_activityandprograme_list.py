'''
Code description: 服务详情
Create time: 2020/12/3
Developer: 叶修
'''
import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml
from api.api_service1 import Api_Auth_Service
import urllib3,json
urllib3.disable_warnings()

testdata = ReadYaml("auth_service1.yaml").get_yaml_data()  # 读取数据


@allure.feature('活动项目详情')
class Test_Programe_List(object):
    log = Log()

    @pytest.mark.process
    @pytest.mark.parametrize('pageNum,pageSize,activityId,expect',testdata['activityandprograme_list'],
                             ids=['活动项目详情'])
    def test_programe_info(self,pageNum,pageSize,activityId,expect):
        self.log.info('%s{%s}' % ((sys._getframe().f_code.co_name,'------项目详情接口-----')))
        # with allure.step('获取活动id'):
        #     activityId = Api_Auth_Service().get_service_id()
        with allure.step('项目详情'):
            msg = Api_Auth_Service().api_activityandprogram_list()
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        # 断言
        # assert msg.json()["result_message"] == expect['result_message']
        # assert msg.json()['result_code'] == expect['result_code']
        # assert 'url' in msg.json()['data']
        assert msg.json()["msg"] == expect['result_message']
        #assert msg.text[0] == expect[0]
        #assert msg.text["code"][0] == json.loads(expect["result_code"])
        #assert 'url' in msg.json()['data']

if __name__ == '__main__':
    pytest.main()
