# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

# from scrapy import signals
import random
import base64

from .settings import USER_AGENTS
from .settings import PROXIE

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        # print(user_agent)
        request.headers.setdefault('User-Agent', user_agent)


class RandomProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIE)
        if proxy.get('user_passwd', '') == '':
            request.meta['proxy'] = 'http://' + proxy.get('ip')
        else:
            request.meta['proxy'] = 'http://' + proxy.get('ip')
            # 对账户密码进行 base64 编码
            base64_up = base64.b64encode(proxy['user_passwd'].encode('utf-8'))
            # 对应到 request 对应的头信息中
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_up.decode('utf-8')


