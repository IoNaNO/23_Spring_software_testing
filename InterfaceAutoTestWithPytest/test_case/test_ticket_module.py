import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util

order_test_data = excel_util.get_sheet_data("用户下单")


@allure.feature("票务模块")
# @pytest.mark.dependency(name="TestTicketModule", depends=["TestLoginModule"], scope='package')
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
    def test_create(self, case_data):
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