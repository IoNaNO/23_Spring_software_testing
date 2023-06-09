from flask import Blueprint, request
import datetime

cash_test = Blueprint('cash', __name__)


def get_single_resp(result, state, test_time):
    return {'actual': result, 'test_result': state, 'test_time': test_time}


@cash_test.route('/test', methods=['GET', 'POST'])
def test():
    test_list = request.json['cash_test_list']
    test_result = []
    for case in test_list:
        start = datetime.datetime.now()
        minutes = int(case['X'])
        late = int(case['Y'])
        expectation = float(case['expectation'])
        if minutes < 0 or late < 0 or minutes > 44640 or late >= 12:
            result = -1.0
        else:
            if minutes <= 60 and late <= 1:
                discount = 0.01
            elif minutes > 60 and minutes <= 120 and late <= 2:
                discount = 0.015
            elif minutes > 120 and minutes <= 180 and late <= 3:
                discount = 0.02
            elif minutes > 180 and minutes <= 300 and late <= 3:
                discount = 0.025
            elif minutes > 300 and late <= 6:
                discount = 0.03
            else:
                discount = 0

            result = float(25+(1-discount)*0.15*minutes)
        if abs(result-expectation) < 0.01:
            state = '测试通过'
        else:
            state = '测试未通过'
        end = datetime.datetime.now()
        span = (end - start).microseconds
        # print(result, expectation, state)
        test_result.append(get_single_resp(round(result, 2), state, f'{span} μs'))
    res = {'test_result': test_result}
    return res