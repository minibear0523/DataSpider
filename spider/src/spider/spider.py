# encoding=UTF-8
import requests as req
from multiprocessing.dummy import Pool as ThreadPool


class Spider:
    def __init__(self, resource):
        """
        初始化相关参数, 包括线程池, 资源类等信息
        :param resource: 资源
        """
        super(Spider, self).__init__()
        self.resource = resource
        self.pool = ThreadPool(resource.pool_limit)

    def set_up(self):
        """
        根据
        :return:
        """