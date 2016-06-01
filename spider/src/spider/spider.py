# encoding=UTF-8
import requests as req
from multiprocessing.dummy import Pool as ThreadPool


class FitTimeSpider:
    REQUEST_LIMIT = 200

    def __init__(self, config):
        """
        初始化相关参数, 包括线程池, 资源类等信息
        :param resource: 资源
        """
        self.config = config
        self.pool = ThreadPool(config.POOL_LIMIT)

    def __set_up_(self):
        """
        初始化相关的逻辑
        """
        pass

    def __form_url_(self, path_type, params):
        """
        生成对应的url
        :param path_type: API的path
        :param params: 对应的参数
        :return: url字符串
        """


    def start(self, index):
        """
        开始抓取
        :param index: 开始抓取的序列id
        :return:
        """
        pass