'''
Code description:配置信息
Create time: 2020/12/3
Developer: 叶修
'''
import os
import pytest
from api.get_token import Get_Token
from common.http_requests1 import HttpRequests
import allure
from config.conf import ConfigManger


@pytest.fixture(scope="session")
def get_token():
    '''前置操作获取token并传入headers'''
    #Get_Token().get_token()
    #if not HttpRequests().params.get("access_token", ""):#没有get到token，跳出用例
    if not HttpRequests().headers.get("token", ""):  # 没有get到token，跳出用例
        pytest.skip("未获取到token跳过用例")
    # value=Get_Token().get_token()
    # HttpRequests().headers.get("Token",value)
    # if not HttpRequests().headers.get("Token", ""):  # 没有get到token，跳出用例
    #     pytest.skip("未获取token跳过用例")
        yield HttpRequests().req
    HttpRequests().req.close()

@pytest.fixture(scope='session')
def headers():
    return {'Token':{0}.format(Get_Token().get_token())}

def pytest_addoption(parser):
    parser.addoption(
        #"--cmdhost", action="store", default="http://192.168.1.54:32099",
        "--cmdhost", action="store", default="https://portal.summer-ospp.ac.cn/summer",
        #"--cmddomain",a
        help="my option: type1 or type2"
    )
@pytest.fixture(scope="session",autouse=True)
#def host(request):
def host(request):
    '''获取命令行参数'''
    #获取命令行参数给到环境变量
    #pytest --cmdhost 运行指定环境
    os.environ["host"] = request.config.getoption("--cmdhost")
    print("当前用例运行测试环境:%s" % os.environ["host"])

# @pytest.hookspec(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#         当测试失败的时候，自动截图，展示到html报告中
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             screen_img = _capture_screenshot()
#             if screen_img:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra