import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util

request_test_data = excel_util.get_sheet_data("查询分享")
add_test_data = excel_util.get_sheet_data("创建分享")

@allure.feature("分享模块")
class TestSharingModule:
    @allure.story("添加分享功能")
    @allure.title('添加分享')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口添加分享')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=1)   # 执行顺序
    @pytest.mark.parametrize('case_data', add_test_data)
    def test_add_create(self,case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("查询分享功能")
    @allure.title('查询分享')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口查询分享')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=2)  # 执行顺序
    @pytest.mark.parametrize('case_data', request_test_data)
    def test_request_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

if __name__ == '__main__':
    test_dir = os.path.dirname(__file__)
    pytest.main(['-s', '-q', test_dir, '--alluredir', '../test_result/', "--clean-alluredir"])
    os.system('allure generate ../test_result/ -o ../test_report/ --clean')
    os.system('allure open -h 127.0.0.1 -p 8881 ../test_report/')