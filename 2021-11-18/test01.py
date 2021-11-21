import requests
import pytest


def test_get():
    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    url = 'http://www.baidu.com'
    data = {
        "name": "zhangshan",
        "age": 21
    }
    ret = requests.get(url=url, verify=False)

