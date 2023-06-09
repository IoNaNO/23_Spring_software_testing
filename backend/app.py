from flask import Flask
from flask_cors import CORS
from tests import *

app = Flask(__name__)
CORS(app)


app.register_blueprint(calendar_test, url_prefix='/api/calendar')
app.register_blueprint(pc_sales_test, url_prefix='/api/sales')
app.register_blueprint(triangle_test, url_prefix='/api/triangle')
app.register_blueprint(cash_test, url_prefix='/api/cash')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
