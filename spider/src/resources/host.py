# encoding=UTF-8
# 资源管理组件, 主要用来管理网站, 网站url等相关配置

class Resources:
    def __init__(self, host, APIs):
        """
        资源类管理初始化
        :param host: 爬虫网站HOST
        :param APIs: API的列表, dict类型, 包含对应的url和parameters
        """
        super.__init__()
        self.host = host
        self.api_list = APIs
        self.parameters = {}

    def set_pool_limit(self, limit):
        self.pool_limit = limit