# encoding=UTF-8
from redis import Redis
from rq import Queue


q = Queue(connection=Redis())


def output_result(results):
    job = q.enqueue()
