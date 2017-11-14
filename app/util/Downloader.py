import requests
from lxml import html

from common import constants
from . import crawl_sleep, get_proxy, generate_http_header, delete_proxy
from .Log import crawler_log


class HtmlDownloader(object):
    def __init__(self, url=constants.HOME_URL):
        self.url = url

    def make_request(self, retry=0):

        crawl_sleep()

        proxy = get_proxy()
        proxies = dict()
        proxies['https'] = 'https://' + proxy

        try:
            res = requests.get(self.url, headers=generate_http_header(), proxies=proxies, timeout=5)
            if res.status_code == 200:
                tree = html.fromstring(res.text)
                return tree
            else:
                crawler_log.info('when crawl {}, get {}'.format(self.url, res.status_code))
                delete_proxy(proxy)
                return self.make_request()
        except requests.exceptions.RequestException as e:
            crawler_log.info('when crawl {}, error is: {}'.format(self.url, e))
            delete_proxy(proxy)
            if retry < 10:
                return self.make_request(retry=retry+1)
            raise
