import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util

register_test_data = excel_util.get_sheet_data("用户注册")
login_test_data = excel_util.get_sheet_data("用户登录")
require_test_data=excel_util.get_sheet_data("查询观演人")
add_test_data = excel_util.get_sheet_data("添加观演人")

@allure.feature("用户模块")
class TestUserModule:
    @allure.story("用户注册功能")
    @allure.title('用户注册')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口注册用户')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=1)   # 执行顺序
    @pytest.mark.parametrize('case_data', register_test_data)
    def test_register_create(self,case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("用户登录功能")
    @allure.title('用户登录')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口登录用户')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=2)   # 执行顺序
    @pytest.mark.parametrize('case_data', login_test_data)
    def test_login_create(self,case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("添加观演人功能")
    @allure.title('添加观演人')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口添加观演人')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=3)   # 执行顺序
    @pytest.mark.parametrize('case_data', add_test_data)
    def test_add_create(self,case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("查询观演人功能")
    @allure.title('查询观演人')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口查询观演人')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=4)   # 执行顺序
    @pytest.mark.parametrize('case_data', require_test_data)
    def test_require_create(self,case_data):
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