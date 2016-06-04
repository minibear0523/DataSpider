# encoding=UTF-8
from flask import Flask, redirect


app = Flask(__name__)


@app.route('/task')
def get_task():
    """
    用于客户端获取任务
    :return:
    """
