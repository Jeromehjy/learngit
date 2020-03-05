import requests
import time
from functools import wraps
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


def get_page(url, options={}):
    """
    抓取网页返回html
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers, **options)
    print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            return response
    except ConnectionError:
        print('抓取失败', url)
        return None

def CountTime(func):
    @wraps(func)
    def wapper(*args,**kwarg):
        start = time.time()
        func(*args,**kwarg)
        end = time.time()
        print(f'{func.__name__.title()}  耗时：{end-start}秒')
    return wapper

if __name__ == "__main__":
    @CountTime
    def test(num,*args,**kwarg):
        time.sleep(num)
        print(f'num:{num}  args:{args}  kwarg:{kwarg}')

    test(4,4,6,k1=2,k2=3)