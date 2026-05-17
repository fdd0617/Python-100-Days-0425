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


# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.getenv("TIANAPI_KEY")
# if not api_key:
#     raise ValueError("TIANAPI_KEY not set")

# url = "http://api.tianapi.com/guonei/"
# params = {
#     "key": api_key,
#     "num": 10
# }
# try:
#     # 再URL中无法读取api_key变量，会当成文本拼上去 
#     # resp = requests.get('http://api.tianapi.com/guonei/?key=api_key&num=10')
#     resp = requests.get(url, params=params, timeout=10)

#     if resp.status_code == 200:
#         data_model = resp.json()
#         for news in data_model['newslist']:
#             print(news['title'])
#             print(news['url'])
#             print('-' * 60)
#     else:
#         print('请求失败，状态码：', resp.status_code)

# except requests.exceptions.RequestException as e:
#     print('网络请求出错：', e)


# **Day 22 练习题（3道）：**

# **题目1：** 创建一个字典包含你的个人信息（姓名、年龄、爱好列表），
# 用 `json.dumps` 转为 JSON 字符串并打印，再用 `json.loads` 还原为字典并打印验证。
person_info = {
    "name":'范斗斗',
    "age":30,
    "hobby":["reading", "music", "travel"]
}
json_info = json.dumps(person_info)
print(json_info)
new_info = json.loads(json_info)
print(new_info)

# **题目2：** 编写程序，将一个包含多个学生信息（姓名、成绩）的列表写入 `students.json` 文件，
# 然后从文件中读取并计算所有学生的平均成绩。

students = [
    {
        "name": "张三",
        "grade": {"Chinese": 66, "Math": 88, "English": 90}
    },
    {
        "name": "李四",
        "grade": {"Chinese": 75, "Math": 92, "English": 84}
    },
    {
        "name": "王五",
        "grade": {"Chinese": 80, "Math": 78, "English": 95}
    }
]


file_path = Path(__file__).parent / 'students.json'
# 把Python对象写入json文件
with open(file_path,'w', encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=2)

with open(file_path,'r',encoding='utf-8') as file:
    new_students = json.load(file)

print(new_students)

all_scores = []
for student in new_students:
    scores = list(student['grade'].values())
    student_avg = sum(scores) / len(scores)
    # 拼接
    all_scores.extend(scores)
    print(f'{student["name"]} 的平均分：{student_avg:.2f}')


# class_avg = sum(all_scores) / len(all_scores)
# print(f'所有学生的总平均分：{class_avg:.2f}')
# **题目3：** 使用 `requests` 库访问一个公开的免费 API（如 `https://httpbin.org/get`），
# 打印返回的状态码和 JSON 内容。如果请求失败，用 `try...except` 处理网络异常。


import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv('TIANAPI_KEY')

url = "http://api.tianapi.com/guonei/"
params = {
    "key": api_key,
    "num": 10
}

try:
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