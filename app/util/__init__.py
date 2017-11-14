import random
import requests
from time import sleep

from common import constants, config


def generate_http_header():
    header = constants.HTTP_HEADER
    header['User-Agent'] = random.choice(constants.USER_AGENT_LIST)
    return header


def get_proxy():
    result = requests.get("{}get/".format(config.PROXY_SERVER_URL))
    if result.status_code == 500:
        sleep(600)
        return get_proxy()
    return result.text


def delete_proxy(proxy):
    requests.get("{}delete/?proxy={}".format(config.PROXY_SERVER_URL, proxy))


def crawl_sleep():
    sleep(random.uniform(constants.MIN_SLEEP_TIME, constants.MAX_SLEEP_TIME))

