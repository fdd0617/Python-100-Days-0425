# json.dump() 把Python写入json文件
# json.dumps() 把Python对象转换成json字符串
# json.load() 从json文件中读取并转换成Python对象
# json.loads() 把json对象转换成Python对象


import json
from pathlib import Path

# my_dict = {
#     'name': '骆昊',
#     'age': 40,
#     'friends': ['王大锤', '白元芳'],
#     'cars': [
#         {'brand': 'BMW', 'max_speed': 240},
#         {'brand': 'Audi', 'max_speed': 280},
#         {'brand': 'Benz', 'max_speed': 280}
#     ]
# }

# file_path = Path(__file__).parent / 'data.json'
# with open(file_path, 'w') as file:
#     json.dump(my_dict, file)


# file_path = Path(__file__).parent / 'data.json'
# with open(file_path, 'r') as file:
#     my_dict = json.load(file)
#     print(type(my_dict))
#     print(my_dict)


import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TIANAPI_KEY")
if not api_key:
    raise ValueError("TIANAPI_KEY not set")

url = "http://api.tianapi.com/guonei/"
params = {
    "key": api_key,
    "num": 10
}
try:
    # 再URL中无法读取api_key变量，会当成文本拼上去 
    # resp = requests.get('http://api.tianapi.com/guonei/?key=api_key&num=10')
    resp = requests.get(url, params=params, timeout=10)

    if resp.status_code == 200:
        data_model = resp.json()
        for news in data_model['newslist']:
            print(news['title'])
            print(news['url'])
            print('-' * 60)
    else:
        print('请求失败，状态码：', resp.status_code)

except requests.exceptions.RequestException as e:
    print('网络请求出错：', e)