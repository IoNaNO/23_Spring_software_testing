import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util

order_test_data = excel_util.get_sheet_data("用户下单")
all_test_data=excel_util.get_sheet_data("查询订单")
detail_test_data = excel_util.get_sheet_data("查询门票详细信息")
show_test_data = excel_util.get_sheet_data("查询演出信息与场次")
qr_test_data = excel_util.get_sheet_data("验票并返回票卷二维码")
location_test_data = excel_util.get_sheet_data("相关地点")
rshow_test_data = excel_util.get_sheet_data("地点相关演出")

# @pytest.mark.dependency(name="TestTicketModule", depends=["TestLoginModule"], scope='package')
@allure.feature("票务模块")
class TestTicketModule:

    # def setup_class(self):
    #     初始化调用注册和登录接口，获取userid和token供后续接口关联
    #     使用该初始化则可不依赖test_login_module.py的TestLoginModule
    #     get_userid_and_token()

    @allure.story("用户下单功能")
    @allure.title('用户下单')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口创建订单')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=1)   # 执行顺序
    @pytest.mark.parametrize('case_data', order_test_data)
    def test_order_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("获得订单功能")
    @allure.title('查询指定用户的所有订单')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口获取所有订单')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=2)   # 执行顺序
    @pytest.mark.parametrize('case_data', all_test_data)
    def test_all_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])   

    @allure.story("查询门票功能")
    @allure.title('查询门票详细信息')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口获取详细信息')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=3)   # 执行顺序
    @pytest.mark.parametrize('case_data', detail_test_data)
    def test_detail_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])   

    @allure.story("查询演出信息")
    @allure.title('用户查看演出信息')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口获取演出信息')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=4)   # 执行顺序
    @pytest.mark.parametrize('case_data', show_test_data)
    def test_show_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])   
    
    @allure.story("验票功能")
    @allure.title('用户验票')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口验票')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=5)   # 执行顺序
    @pytest.mark.parametrize('case_data', qr_test_data)
    def test_qr_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("地点功能")
    @allure.title('演出相关地点')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口获取演出相关地点')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=6)   # 执行顺序
    @pytest.mark.parametrize('case_data', location_test_data)
    def test_location_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("演出推荐功能")
    @allure.title('地点相关演出')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口获取地点相关演出')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=7)   # 执行顺序
    @pytest.mark.parametrize('case_data', rshow_test_data)
    def test_rshow_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])


if __name__ == "__main__":
    test_dir = os.path.dirname(__file__)
    pytest.main(['-s', '-q', test_dir, '--alluredir', '../test_result/', "--clean-alluredir"])
    os.system('allure generate ../test_result/ -o ../test_report/ --clean')
    os.system('allure open -h 127.0.0.1 -p 8881 ../test_report/')