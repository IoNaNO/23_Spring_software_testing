from flask import Blueprint, request
from flask_cors import CORS
import datetime

calendar_test = Blueprint('calendar', __name__)


def get_single_resp(a, i, t: bool):
    return {'actual': a, 'info': i, 'test_result': '测试通过' if t else '测试未通过'}


@calendar_test.route('/test', methods=['GET', 'POST'])
def test():
    test_list = request.json['calendar_test_list']
    test_result = []
    for case in test_list:
        year = int(case['year'])
        month = int(case['month'])
        day = int(case['day'])
        expectation = case['expectation']
        info = ""
        _date = "-1"
        if year < 2000 or year > 2100:
            info += "Year out of range,\n"
        if month < 1 or month > 12:
            info += "Month out of range,\n"
        if day < 1 or day > 31:
            info += "Day out of range,\n"
        if info != "":
            info.strip()
            test_result.append(get_single_resp(_date, info, _date == expectation))
            continue
        try:
            _date = datetime.datetime.strptime('-'.join([str(year), str(month), str(day)]), '%Y-%m-%d').date()
            _date = str(_date + datetime.timedelta(days=1))
        except Exception as e:
            info += "Day out of range for month,\n"
            _date = "-1"
        info.strip()
        test_result.append(get_single_resp(_date, info, _date == expectation))
    res = {'test_result': test_result}
    return res
