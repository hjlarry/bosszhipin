
# HTTP相关配置

HTTP_HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,th;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Cookie': '__c=1504495757; __g=-; lastCity=100010000; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1504495759; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1505281142; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2F; __a=70993408.1504495757..1504495757.164.1.164.164',
    'Host': 'www.zhipin.com',
    'Referer': 'https://www.zhipin.com/c100010000-p210101/?page=2&ka=page-2',
    'Upgrade-Insecure-Requests': '1'
}

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
    "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 360Browser"
]


# JOB相关配置

FINANCE_STAGE_DICT = {
    'unknown': 0,
    '未融资': 1,
    '天使轮': 2,
    'A轮': 3,
    'B轮': 4,
    'C轮': 5,
    'D轮及以上': 6,
    '已上市': 7,
    '不需要融资': 8
}

WORK_YEARS_REQUEST_DICT = {
    'unknown': 0,
    '应届生': 1,
    '1年以内': 2,
    '1-3年': 3,
    '3-5年': 4,
    '5-10年': 5,
    '10年以上': 6,
    '经验不限': 7
}

EDUCATION_REQUEST_DICT = {
    'unknown': 0,
    '中专及以下': 1,
    '高中': 2,
    '大专': 3,
    '本科': 4,
    '硕士': 5,
    '博士': 6,
    '不限': 7,
}

COMPANY_SIZE_DICT = {
    'unknown': 0,
    '0-20人': 1,
    '20-99人': 2,
    '100-499人': 3,
    '500-999人': 4,
    '1000-9999人': 5,
    '10000人以上': 6
}

INDUSTRY_DICT = {
    'unknown': 0,
    '健康医疗': 1,
    '生活服务': 2,
    '旅游': 3,
    '金融': 4,
    '信息安全': 5,
    '广告营销': 6,
    '数据服务': 7,
    '智能硬件': 8,
    '文化娱乐': 9,
    '网络招聘': 10,
    '分类信息': 11,
    '电子商务': 12,
    '移动互联网': 13,
    '企业服务': 14,
    '社交网络': 15,
    '教育培训': 16,
    'O2O': 17,
    '游戏': 18,
    '互联网': 19,
    '媒体': 20,
    'IT软件': 21,
    '通信': 22,
    '公关会展': 23,
    '房地产/建筑': 24,
    '汽车供应链/物流': 25,
    '咨询/翻译/法律': 26,
    '采购/贸易': 27,
    '非互联网行业': 28
}


# crawl相关配置
HOME_URL = 'https://www.zhipin.com'
MIN_SLEEP_TIME = 1
MAX_SLEEP_TIME = 3


