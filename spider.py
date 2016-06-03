# encoding=UTF-8
import json
import requests as req
from multiprocessing.dummy import Pool as ThreadPool


HOST = 'https://api.rjft.net'
USER_ID_LIMIT_PER_CLIENT = 200
USER_ID_TOTAL_COUNT = 11406044
USER_MAX_ACTIVITY_COUNT = 2000


def _form_url(user_id):
    url = '/'.join([HOST, 'social', 'user', str(user_id), 'activity'])
    url = url + '?before=&count=' + str(USER_MAX_ACTIVITY_COUNT)
    return url

def parse_result(self, content):
    data = None
    try:
        # json loads response's content to json object.
        data = json.loads(content)['result']
    except Exception, e:
        print e
        return []

    # parse json object
    result = []
    for activity in data:
        result.append({
            'user_id': activity['user_id'],
            'id': activity['id'],
            'content': activity['content'],
            'create_time': activity['create_time'],
            'update_time': activity['update_time']
            'total_comment': activity['total_comment'],
            'total_praise': activity['total_praise'],
            'video_url': activity['video_url'],
            'image_url': activity['image'][0]['url'],
        })
    return result

def request_user_social_activity_list(url):
    res = req.get(url).content
    return res