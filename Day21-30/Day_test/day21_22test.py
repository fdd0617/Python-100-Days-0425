# 可以。根据这两章 [21.文件读写和异常处理.md](/Users/fan/Projects/Python-100-Days-0425/Day21-30/21.文件读写和异常处理.md) 和 [22.对象的序列化和反序列化.md](/Users/fan/Projects/Python-100-Days-0425/Day21-30/22.对象的序列化和反序列化.md) 的内容，我给你出一组按难度递进的练习题，覆盖：

# - 文本文件读写
# - `with` 上下文管理器
# - 异常处理
# - 自定义异常
# - JSON 的 `dump / dumps / load / loads`
# - 简单的网络 API / JSON 数据处理思路

# **基础题**

# 1. 编写程序，读取 `log.txt` 的全部内容并打印。
# 要求：
# - 使用 `with open(...)`
# - 指定 `encoding='utf-8'`

# from pathlib import Path
# file_path = Path(__file__).parent / 'log.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     print(file.read())

# 2. 编写程序，逐行读取 `log.txt`，并在每一行前面加上行号输出。
# 示例：
# ```python
# 1: 第一行内容
# 2: 第二行内容
# ```
# from pathlib import Path
# file_path = Path(__file__).parent / 'log.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
# #     content = file.read().splitlines()
# #     # print(content)
# # for index, line in enumerate(content, start=1):
# #     print(f"{index}: {line}")
#       for line_no, line in enumerate(file, start=1):
#             print(f"{line_no}: {line.rstrip()}")

# # names = ['A', 'B', 'C']
# # for name in names:
# #     print(name)

# # for index, name in enumerate(names, start=1):
# #     print(f"{index}: {name}")

# 3. 编写程序，向 `notes.txt` 中写入三行文字。
# 要求：
# - 使用写入模式 `w`
# - 再用追加模式 `a` 追加一行“写入结束”

# from pathlib import Path
# file_path = Path(__file__).parent / 'notes.txt'
# with open(file_path, 'w', encoding='utf-8') as file:
#     content1 = '第一行\n'
#     content2 = '第二行\n'
#     content3 = '第三行\n'
#     file.write(content1)
#     file.write(content2)
#     file.write(content3)

# with open(file_path, 'w', encoding='utf-8') as file:
#     content2 = '第二行\n'
#     file.write(content2)

# with open(file_path, 'w', encoding='utf-8') as file:
#     content3 = '第三行\n'
#     file.write(content3)

# with open(file_path, 'a', encoding='utf-8') as file:
#     content4 = '写入结束\n'
#     file.write(content4)

# 4. 编写函数 `count_lines(filepath)`，返回文件一共有多少行。
# 要求：
# - 文件不存在时捕获异常
# - 出错时返回 `0`


# def count_lines(filepath):
#     try:
#         with open(filepath, 'r', encoding='utf-8') as file:
#             # return sum(1 for _ in file)  #文件每读取一行，加 1
#             content = len(file.read().splitlines())
#             return content
        
#     except FileNotFoundError:
#         print('文件不存在')
#         return 0

# from pathlib import Path
# file_path = Path(__file__).parent / 'log.txt'
# res = count_lines(file_path)
# print(res)

# **进阶题**

# 5. 编写函数 `safe_copy(src, dst)`，将一个文本文件内容复制到另一个文件。
# 要求：
# - 使用 `with`
# - 捕获 `FileNotFoundError`
# - 捕获 `UnicodeDecodeError`
# - 复制成功后打印“复制完成”
# from pathlib import Path
# def safe_copy(src, dst):
#     try:
#         # with open(src, 'r', encoding='utf-8') as file1:
#         #     with open(dst, 'w', encoding='utf-8') as file2:
#         # 优化成一个 with 同时打开两个文件：
#         with open(src, 'r', encoding='utf-8') as file1,\
#              open(dst, 'w', encoding='utf-8') as file2:
#                 # file2.write(file1.read())
#                 # 逐行复制
#                 for line in file1:
#                      file2.write(line)

#     except FileNotFoundError:
#         print('文件不存在')
#     except UnicodeDecodeError:
#         print('编码错误')
#     else:
#         print('复制完成')

# src = Path(__file__).parent / 'log.txt'
# dst = Path(__file__).parent / 'log1.txt'

# safe_copy(src, dst)

# 6. 编写函数 `word_count(filepath)`，统计一个文本文件中每个单词出现的次数。
# 要求：
# - 不区分大小写
# - 返回字典
# - 例如：`{"python": 3, "file": 2}`
# import re
# from pathlib import Path
# def word_count(filepath):
#     try:
#         with open(filepath, 'r', encoding='utf-8') as file:
#             all_counts = {}
#             # 全部转换成小写
#             content = file.read().lower()
#             # 单词用空白分割  使用split() 标点符号不会比处理，只是按照空白分割。
#             # words = content.split()
#             # re.findall() 会从整段文本里，所有符合规则的内容找出来。并放进一个列表
#             words = re.findall(r'[a-z]+', content)
#             for word in words:
#                 all_counts[word] = all_counts.get(word, 0) + 1
#             return all_counts
    
#     except FileNotFoundError:
#         print('文件不存在')
#         return {}


# file_path = Path(__file__).parent / 'log1.txt'
# res = word_count(file_path)
# print(res)

# 7. 自定义异常 `EmptyFileError`
# 要求：
# - 当读取的文件内容为空时，抛出 `EmptyFileError("文件内容为空")`
# - 在调用处用 `try/except` 捕获并打印错误信息

# from pathlib import Path
# # 自定义异常
# class EmptyFileError(ValueError):
#     pass

# file_path = Path(__file__).parent / 'log1.txt'
# try:
#     # 打开文件
#     with open(file_path, 'r', encoding='utf-8') as file:
#         # 访问文件，file.read()读取一次 指针已经到末尾了，后面不能在使用read了，因此要先存到变量里。
#         content = file.read()
#         if not content:
#             # 判断文件是否为空，主动抛出异常。并携带自定义信息
#             raise EmptyFileError('文件内容为空')
#         print(content)
# # 捕获异常 EmptyFileError 
# except EmptyFileError as e:
#         print(e)

# 8. 编写程序复制一张图片。
# 要求：
# - 以二进制模式打开原文件
# - 以二进制模式写入新文件
# - 文件名例如：`source.jpg -> backup.jpg`


# from pathlib import Path
# def copy_picture(old_path,new_path):

#     # 二进制读取 rb 
#     with open(old_path,'rb') as old:
#         # 二进制写入 wb 
#         with open(new_path,'wb') as new:
#             # 读取内容并写入新图片
#             new.write(old.read())

    
# old_path = Path(__file__).parent / 'copy.png'
# new_path = Path(__file__).parent / 'backup.png'
# try:
#     copy_picture(old_path,new_path)
# except FileNotFoundError:
#     print('文件不存在')
# else:
#     print('复制成功')

# **JSON 练习题**

# 9. 创建一个字典，保存一个学生的信息：
# - 姓名
# - 年龄
# - 爱好列表
# - 成绩字典

# 要求：
# - 用 `json.dumps()` 转成 JSON 字符串并打印
# - 再用 `json.loads()` 还原成 Python 对象并打印类型

# import json
# std_info = {
#     'name':'张三',
#     'age':30,
#     'hobby':['reading','singing','running'],
#     'grade':{'Chinese':98,'Math':80,'English':60}
# }
# # 转换成json字符串时注意，使用ensure_ascii=False 表示中文正常显示，
# content = json.dumps(std_info, ensure_ascii=False)
# print(content)
# res = json.loads(content)
# print(res)
# print(type(res))

# 10. 编写程序，将多个学生信息保存到 `students.json`。
# 每个学生包含：
# - `name`
# - `age`
# - `scores`

# 要求：
# - 使用 `json.dump()`
# - 使用 `ensure_ascii=False`
# - 使用 `indent=2`

# import json
# from pathlib import Path
# std_info = [
#     {'name':'张三','age':28,'scores':[88,90,60]},
#     {'name':'李四','age':28,'scores':[55,86,98]},
#     {'name':'王五','age':28,'scores':[98,90,94]},
#     {'name':'马六','age':28,'scores':[68,100,99]},
# ]

# file_path = Path(__file__).parent / 'students.json'
# with open(file_path, 'w', encoding='utf-8') as file:
#     # ensure_ascii 中文转换   indent=2 内容缩进2空格
#     json.dump(std_info,file, ensure_ascii=False, indent=2)


# 11. 编写程序，从 `students.json` 读取数据并完成下面任务：
# - 打印所有学生姓名
# - 计算每个学生的平均分
# - 计算全班总平均分

# import json
# from pathlib import Path
# file_path = Path(__file__).parent / 'students.json'
# with open(file_path, 'r', encoding='utf-8') as file:
#     # json.load 从json文件中读取，转成Python对象
#     contents = json.load(file)
#     # print(contents)
#     total_grade = 0
#     for content in contents:
#         print(f"{content['name']}:{sum(content['scores'])/len(content['scores']):.2f}")
#         total_grade += sum(content['scores'])
#     print(f"全班总平均分:{total_grade/len(contents)}")

# 12. 编写函数 `append_student(filepath, student_info)`。
# 要求：
# - 从 JSON 文件中读取已有学生列表
# - 将新的学生字典追加进去
# - 再写回 JSON 文件
# - 如果文件不存在，则自动创建并写入一个新列表


# import json
# from pathlib import Path
# def append_student(filepath, student_info):
#     try:
#         # 读取json文件，用json.load() 转换成Python对象 字典 
#         with open(filepath, 'r', encoding='utf-8') as file:
#             students = json.load(file)
#     except FileNotFoundError:
#         students = []
#     # 新学生信息追加到列表中
#     students.append(student_info)
# # 读取文件，将新学生列表转换成json文件 使用 json.dump(Python对象，文件对象),ensure_ascii中文格式显示，indent=2 换行 内容缩进
#     with open(filepath, 'w', encoding='utf-8') as file: 
#         json.dump(students, file, ensure_ascii=False, indent=2)

# file_path = Path(__file__).parent / 'students.json'

# student_info = {'name':'张三A','age':28,'scores':[88,90,60]}

# append_student(file_path, student_info)
# **综合题**

# 13. 编写一个“简易日志系统”。
# 要求：
# - 定义函数 `write_log(filepath, content)`
# - 如果 `content` 是空字符串或 `None`，抛出自定义异常 `EmptyContentError`
# - 正常写入时，使用追加模式，并在每条日志前加时间戳
# - 单独写调用代码捕获异常

# from pathlib import Path
# from datetime import datetime

# class EmptyContentError(ValueError):
#     pass

# def write_log(filepath, content):
#     if not content:
#         raise EmptyContentError('日志为空。')
#     current_time = datetime.now().strftime('%Y-%-%d %H:%M:%S')
#     log_text = f'[{current_time}] {content}\n'
#     with open(filepath, 'a', encoding='utf-8') as file:
#         res = file.write(log_text)

# file_path = Path(__file__).parent / 'log.txt'

# try:
#     write_log(file_path, '程序启动')
#     write_log(file_path, '用户登录')
#     write_log(file_path, '')
# except EmptyContentError as err:
#     print(err)



# 14. 编写一个“配置文件读取器”。
# 假设有 `config.json`，内容类似：
# ```json
# {
#   "host": "127.0.0.1",
#   "port": 8000,
#   "debug": true
# }
# ```
# 要求：
# - 读取 JSON 文件
# - 打印 `host`、`port`、`debug`
# - 如果 JSON 格式错误，捕获异常并提示“配置文件格式错误”

# from pathlib import Path
# import json
# try:
#     file_path = Path(__file__).parent / 'config.json'
#     with open(file_path, 'r', encoding='utf-8') as file:
#         config = json.load(file)
    
#     print('host:', config['host'])
#     print('port:', config['port'])
#     print('debug:', config['debug'])
# except json.JSONDecodeError:
#     print('配置文件格式错误')

# 15. 编写一个“新闻数据模拟处理”程序。
# 不要真正访问网络，直接准备一个模拟的 JSON 字符串：

# ```python
# news_json = '''
# {
#   "newslist": [
#     {"title": "新闻1", "url": "http://example.com/1"},
#     {"title": "新闻2", "url": "http://example.com/2"}
#   ]
# }
# '''
# ```

# 要求：
# - 用 `json.loads()` 转成 Python 对象
# - 遍历 `newslist`
# - 打印每条新闻的标题和链接
# import json



# def news_config(news):
#     try:
#         data = json.loads(news)
#         for news_item in data['newslist']:
#             print(f"标题是：{news_item['title']}")
#             print(f"链接是：{news_item['url']}")
#     except json.JSONDecodeError:
#         print('配置文件格式错误')


# news_json = '''
# {
#   "newslist": [
#     {"title": "新闻1", "url": "http://example.com/1"},
#     {"title": "新闻2", "url": "http://example.com/2"}
#   ]
# }
# '''
# news_config(news_json)

# **拔高题**

# 16. 编写函数 `merge_json_files(file1, file2, target)`。
# 要求：
# - `file1` 和 `file2` 中都保存的是列表数据
# - 读取两个文件中的 JSON 列表
# - 合并成一个列表后写入 `target`
# - 处理文件不存在和 JSON 格式错误的情况

# import json
# from pathlib import Path

# def merge_json_files(file1, file2, target):
#     try:
#         with open(file1, 'r', encoding='utf-8') as f1:
#             # json.load(file)：从json文件读取数据，转换成Python对象
#             data1 = json.load(f1)
#         with open(file2, 'r', encoding='utf-8') as f2:
#             data2 = json.load(f2)

#         # 判断读取出来的数据是不是列表
#         if not isinstance(data1, list) or not isinstance(data2, list):
#             print('JSON文件中保存的不是列表数据')
#             return
#         merged_data = data1 + data2

#         with open(target, 'w', encoding='utf-8') as file:
#             # 把合并后的列表写入新的json文件
#             json.dump(merged_data, file, ensure_ascii=False, indent=2)

#         print("合并完成")

    # except FileNotFoundError:
    #     print('文件不存在')
    # except json.JSONDecodeError:
    #     print('Json格式错误.')


# base_dir = Path(__file__).parent

# file1 = base_dir / 'config.json'
# file2 = base_dir / 'students.json'
# target = base_dir / 'all_data.json'

# merge_json_files(file1, file2, target)



    


# 17. 编写函数 `save_dict_as_json(filepath, data)`。
# 要求：
# - 参数 `data` 必须是字典
# - 如果不是字典，抛出 `TypeError`
# - 如果是字典，写入 JSON 文件
# - 写入成功后打印“保存成功”
# import json
# from pathlib import Path

# def save_dict_as_json(filepath, data):
#     if not isinstance(data, dict):
#         raise TypeError('data 必须是字典')
    
#     with open(filepath, 'w', encoding='utf-8') as file:
#         # 把data 写入 file json.dup(要写入的数据，文件对象)
#         json.dump(data, file, ensure_ascii=False, indent=2)

#     print('保存成功')

# file_path = Path(__file__).parent / 'data.json'

# person = {
#     'name': '张三',
#     'age': 18
# }

# try:
#     save_dict_as_json(file_path,person)
# except TypeError as err:
#     print(err)

# 18. 编写一个小项目：学生成绩管理器。
# 要求：
# - 从 `students.json` 读取学生数据
# - 提供三个函数：
#   - `show_students()`：显示所有学生信息
#   - `add_student()`：添加新学生
#   - `average_score()`：计算某个学生平均分
# - 读写文件时都要使用异常处理
from pathlib import Path
import json


class Student:
    def show_students(self, filepath):
        """显示所有学生信息"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                student_list = json.load(file)
                return student_list
            
        except FileNotFoundError:
            print('文件不存在')
        except json.JSONDecodeError:
            print('Json格式错误.')
        
    def add_student(self, filepath, student_info):
        """添加新学生"""
        try:
            # 不能直接追加， 要先读取json文件，转换后 拼接，再写入json文件
            with open(filepath, 'r', encoding='utf-8') as file:
                student_list = json.load(file)

            student_list.append(student_info)

            with open(filepath, 'w', encoding='utf-8') as file:    
                json.dump(student_list, file, ensure_ascii=False, indent=2)

        except FileNotFoundError:
            print('文件不存在')
        except json.JSONDecodeError:
            print('Json格式错误.')
        else:
            print('添加完成.')

    def average_score(self, filepath, std_name):
        """计算某个学生平均分"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                student_list = json.load(file)
                for std in student_list:
                    if std['name'] == std_name:
                        avg_grade = sum(std['scores'])/len(std['scores'])

                        return f'{std_name}的平均分是： {avg_grade:.2f}'
                return f'没有找到学生：{std_name}'
            
        except FileNotFoundError:
            print('文件不存在')
        except json.JSONDecodeError:
            print('Json格式错误.')      

filepath = Path(__file__).parent / 'students.json'
std = Student()
# std.show_students()
print(std.show_students(filepath))
            
student_info =   {
    "name": "张三B",
    "age": 28,
    "scores": [
      88,
      90,
      60
    ]
  }
std.add_student(filepath, student_info)
print(std.show_students(filepath))

print(std.average_score(filepath, '张三'))



