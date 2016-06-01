# encoding=UTF-8
from ._config import Config
from urllib import urlencode


class FitTimeConfig(Config):
    """
    针对FitTime APP的爬虫配置, 继承_config.Config基类, override HOST参数
    """
    HOST = "https://api.rjft.net"

config = {
    'fittime': FitTimeConfig
}