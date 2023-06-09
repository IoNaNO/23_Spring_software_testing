from flask import Blueprint, request
import datetime

triangle_test = Blueprint('triangle', __name__)


def get_single_resp(state, test_time):
    return {'actual': state, 'test_time': test_time}


@triangle_test.route('/test', methods=['GET', 'POST'])
def test():
    test_list = request.json['triangle_test_list']
    test_result = []
    for case in test_list:
        start = datetime.datetime.now()
        A = int(case['A'])
        B = int(case['B'])
        C = int(case['C'])
        if A < 0 or B < 0 or C < 0:
            result = '不构成三角形'

        elif A + B <= C or B + C <= A or C + A <= B:
            result = '不构成三角形'
        
        elif A == B and B == C:
            result = '等边三角形'

        elif A == B or B == C or C == A:
            result = '等腰三角形'

        else:
            result = '一般三角形'
        
        end = datetime.datetime.now()
        span = (end - start).microseconds

        test_result.append(get_single_resp(result, f'{span} μs'))
    res = {'test_result': test_result}
    return res