from flask import Blueprint, request
import datetime

pc_sales_test = Blueprint('pc_sales', __name__)


def get_single_resp(amount, state, earn, test_time):
    return {'amount': amount, 'actual': state, 'earn': earn, 'test_time': test_time}


@pc_sales_test.route('/test', methods=['GET', 'POST'])
def test():
    test_list = request.json['sales_test_list']
    test_result = []
    for case in test_list:
        start = datetime.datetime.now()
        host_num = int(case['M'])
        if host_num == -1:
            test_result.append(get_single_resp('-', '自动统计', '-', '-'))
            continue
        display_num = int(case['I'])
        peripheral_num = int(case['P'])
        if host_num <= 0 or display_num <= 0 or peripheral_num <= 0 or host_num > 70 or display_num > 80 or peripheral_num > 90:
            test_result.append(get_single_resp('-', '异常', '-', '-'))
            continue
        commission = host_num * 25 + display_num * 30 + peripheral_num * 45
        end = datetime.datetime.now()
        span = (end - start).microseconds
        if commission <= 1000:
            test_result.append(get_single_resp(commission, '正常', float('%.2f' % (commission * 0.1)), f"{span} μs"))
        elif commission <= 1800:
            test_result.append(get_single_resp(commission, '正常', float('%.2f' % (commission * 0.15)), f"{span} μs"))
        else:
            test_result.append(get_single_resp(commission, '正常', float('%.2f' % (commission * 0.2)), f"{span} μs"))
    res = {'test_result': test_result}
    return res
