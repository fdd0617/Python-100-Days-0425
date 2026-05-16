from datetime import datetime, time
from pathlib import Path


# 读取文件
# file_path = Path(__file__).parent / '致橡树.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     # print(file.read())
#     for line in file:
#         print(line, end='')

# 写入文件（写入前检查是否已有，避免重复追加）
# file_path = Path(__file__).parent / '致橡树.txt'
# append_text = '\n标题：《致橡树》\n作者：舒婷\n时间：1977年3月'

# with open(file_path, 'r', encoding='utf-8') as file:
#     if '标题：《致橡树》' not in file.read():
#         with open(file_path, 'a', encoding='utf-8') as file:
#             file.write(append_text)

# with open(file_path, 'r', encoding='utf-8') as file:
#     print(file.read())

# 异常处理机制 try后面跟代码块 except后面跟异常处理 else后面跟 try 中的代码没有异常时执行的代码
#  finally 无论是否异常都会执行
# raise 抛出自定义提示的异常 → except 捕获后用自定义提示替换原始报错。

# class InputError(ValueError):
#     pass

# def fac(num):
#     """求阶乘"""
#     if num < 0:
#         # rasie 抛出异常 携带自定义的提示输出  
#         # 创建一个 InputError 异常对象，携带自定义提示信息 主动抛出这个异常，中断当前函数执行
#         raise InputError("只能计算非负整数的阶乘")
#     if num in (0,1):
#         return 1
#     return num * fac(num - 1)

# flag = True
# while flag:
#     num = int(input("n = "))
#     try:
#         print(f"{num}! = {fac(num)}")
#         flag = False
#     # 捕获异常，InputError 捕获后用自定义提示替换原始报错。
#     except InputError as err:
#         print(err)

#     else:
#         print(f"else也执行了")


#     finally:
#         print("finally都会执行")



# 练习1：文件读取与统计

# 读取 致橡树.txt，统计文件中有多少行、多少个字符（不含换行符），将统计结果打印出来。
# file_path = Path(__file__).parent / '致橡树.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
#     # splitlines() 按照换行把文本拆成一行一行的列表
#     line_count = len(content.splitlines())
#     # 去掉换行符，统计所有字符数
#     char_count = len(content.replace('\n', ''))

# print(f'行数：{line_count}')
# print(f'字符数（不含换行符）：{char_count}')

# 练习2：异常处理 - 安全的类型转换

# 写一个函数 safe_int(value)，将输入转为整数。如果转换失败，捕获 ValueError 并返回 None。
# 测试：safe_int("123")、safe_int("abc")、safe_int("")。

# def safe_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         return None
    
# print(safe_int("123"))
# print(safe_int("abc"))
# print(safe_int(""))


# 练习3：自定义异常 - 成绩验证

# 自定义异常 ScoreError，写一个函数 check_score(score)，当成绩不在 0~100 范围内时抛出 
# ScoreError("成绩必须在0-100之间")。调用时用 try...except 捕获并提示，输入合法时打印成绩等级。

# class ScoreError(ValueError):
#     pass

# def check_score(score):
#     if score < 0 or score > 100:
#         raise ScoreError("成绩必须在0-100之间")
#     elif score >= 90:
#         return "你的等级是A"
#     elif score >= 60:
#         return "你的等级是B"
#     else:
#         return "你的等级是C"
# try:
#     score = int(input("请输入你的成绩："))
#     res = check_score(score)
#     print(res)

# except ScoreError as err:
#     print(err)

# except ValueError:
#     print("请输入整数。")

# 练习4：文件写入与追加

# 创建一个日志记录程序：每次运行时将当前时间追加写入 log.txt，格式为 [2026-05-13 14:30:00] 程序启动。
# 如果文件不存在则创建，已存在则追加。用 try...except 处理可能的写入异常。
# file_path = Path(__file__).parent / 'log.txt'

# try:

#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     long_text = f"[{current_time}] 程序启动\n"

#     # w 覆盖写入 a 追加写入
#     with open(file_path, 'a', encoding='utf-8') as file:
#         file.write(long_text)
    
# except OSError as err:
#     print(f"写入日志失败：{err}")
    


# 练习5：二进制文件复制（进阶）

# 用分块读写的方式（每次 1024 字节）复制一个图片文件，并用 with 语法管理文件对象。
# 如果源文件不存在，捕获 FileNotFoundError 给出友好提示。

file_path = Path(__file__).parent.parent/'res'/'20210803201644.png'
target_path = Path(__file__).parent/'copy.png'

try:

    # 读取二进制文件 读 rb 写入 wb
    with open(file_path, 'rb' ) as file, open(target_path,'wb') as dst:
        while True:
            # 分块读写，每次读取1024字节
            data = file.read(1024)
            if not data:
                break
            dst.write(data)

except FileNotFoundError as err:
    print(err)