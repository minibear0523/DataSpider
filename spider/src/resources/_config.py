# encoding=UTF-8
# 资源管理组件, 主要用来管理网站, 网站url等相关配置


class Config(object):
    """
    Config基类, 所有config类都需要继承这个类.
    :param HOST: 爬虫的root url
    :param PORT: 爬虫的访问端口, 默认为80
    :param POOL_THREAD_LIMIT: 子线程数, 默认为20
    """
    HOST = ""
    PORT = 80
    POOL_THREAD_LIMIT = 20
