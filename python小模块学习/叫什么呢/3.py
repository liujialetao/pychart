# -*- coding: UTF-8 -*-
import json
import time
import datetime
import urllib
import os, sys
from flask import Flask, jsonify, request

app = Flask(__name__)

MY_URL = '/api/py/'

# http://0.0.0.0:9010/api/py//hhh?a=1&b=2
@app.route(MY_URL + '/hhh', methods=['GET', 'POST'])
def hh_svr():
    param = request.json  # 请求参数
    input_data = param  # str
    input_data1 = param['data1']  # str
    print('input_data', input_data, type(input_data))
    print('input_data1', input_data1)
    # your biz
    return jsonify({'code': 0, 'data': input_data, 'data1': input_data1, 'msg': ""})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True)