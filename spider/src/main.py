# encoding=UTF-8
from resources.fittime import config
from spider.spider import FitTimeSpider


if __name__ == '__main__':
    spider = FitTimeSpider(config['fittime'])
