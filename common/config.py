import redis

REDIS_CONF = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': 'root',
    'broker_db': 5,
    'backend_db': 4,
    'uncrawl_job_des': 1,
    'crawled_job_des': 2,
    'uncrawl_com': 7,
    'crawled_com': 8
}


class RedisConnect(object):
    def __init__(self, db=REDIS_CONF['uncrawl_job_des']):
        self.conn = redis.Redis(host=REDIS_CONF['host'], port=REDIS_CONF['port'], password=REDIS_CONF['password'], db=db)


uncrawl_job_des = RedisConnect(db=REDIS_CONF['uncrawl_job_des']).conn
crawled_job_des = RedisConnect(db=REDIS_CONF['crawled_job_des']).conn
uncrawl_com = RedisConnect(db=REDIS_CONF['uncrawl_com']).conn
crawled_com = RedisConnect(db=REDIS_CONF['crawled_com']).conn


MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': 'root',
    'db': 'boss'
}


PROXY_SERVER_URL = 'http://10.199.4.55:5000/'


class Config:
    DEBUG = True
    SECRET_KEY = 'mybossprogram'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(MYSQL_CONF['username'],MYSQL_CONF['password'], MYSQL_CONF['host'], MYSQL_CONF['port'], MYSQL_CONF['db'])


config = {
    'default': Config
}