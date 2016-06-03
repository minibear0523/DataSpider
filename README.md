# 社会化海量数据采集爬虫框架
参考了[这篇文章](http://www.lanceyan.com/tech/arch/snscrawler.html)

# 分布式方法
使用一个MQ服务, 提供User_ID查询功能, 用来各个分布式节点查询任务.
分布式节点采用multiprocessing的方法, 利用多线程技术来进行抓取, 将结果放到结果队列中, 单独起一个线程用来储存数据到数据库中.