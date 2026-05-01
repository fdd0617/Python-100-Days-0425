
from functools import lru_cache, wraps
import time
import random


# def download(filename):
#     """开始下载文件"""
#     print(f"开始是下载{filename}")
#     time.sleep(random.random()*6)
#     print(f"{filename}下载完成。")

# def upload(filename):
#     """开始下载文件"""
#     print(f"开始上传{filename}")
#     time.sleep(random.random()*8)
#     print(f"{filename}上传完成。")

# start = time.time()
# download('MySQL从删库到跑路.avi')
# end = time.time()
# print(f"花费时间：{end-start:.2f}秒")
# start = time.time()
# upload('Python从入门到住院.pdf')
# end = time.time()
# print(f"花费时间：{end-start:.2f}秒")

# def record_time(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"花费时间：{end-start:.2f}秒")
#         return result
#     return wrapper

# @record_time
# def download(filename):
#     """开始下载文件"""
#     print(f"开始是下载{filename}")
#     time.sleep(random.random()*6)
#     print(f"{filename}下载完成。")

# @record_time
# def upload(filename):
#     """开始下载文件"""
#     print(f"开始上传{filename}")
#     time.sleep(random.random()*8)
#     print(f"{filename}上传完成。")


# # download = record_time(download)
# download('MySQL从删库到跑路.avi')

# download.__wrapped__('MySQL从删库到跑路.avi')

# 阶乘
# def fac(num):
#     if num in (0,1):
#         return 1
#     return num * fac(num - 1)

# res = fac(5000)
# print(res)
# 斐波那契数列 前两项只和等于后一个数 前两位是1,计算第n个
# @lru_cache
# def fib1(n):
#     if n in (1,2):
#         return 1
#     return fib1(n-1) + fib1(n-2)

# for i in range(1,51):
#     print(fib1(i))

# 循环递归方式实现
# def fib2(n):
#     a,b = 0,1
#     for _ in range(n):
#         a,b = b,a+b
#     return a

# for i in range(1,51):
#     print(fib2(i))


# **Day 17 练习题（共3道）**

# **题目1：** 请编写一个装饰器 `log_call`，它能在每次调用被装饰的函数时打印一行日志，格式为 `"调用了函数: 函数名，参数: args, kwargs"`。用 `@log_call` 装饰一个简单的 `add(a, b)` 函数并测试。
def log_call(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"调用了函数：{func.__name__}，参数：{args},{kwargs}")
        result = func(*args,**kwargs)
        return result
    return wrapper

@log_call
def add(a,b):
    return a+b


print(add(1,2))
# **题目2：** 下面的递归函数有什么问题？请指出并修正：
```python
def countdown(n):
    print(n)
    return countdown(n - 2)
```
没有收敛条件，无法停止
# **题目3：** 请分别用递归和循环两种方式实现一个函数 `sum_digits(n)`，计算一个正整数各位数字之和。例如 `sum_digits(12345)` 返回 `15`（即 1+2+3+4+5）。

# # 递归
def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n//10) + n % 10


# 循环
def sum_digits(n):
    sum =0
    for i in str(n):
        sum += int(i)
    return sum

print(sum_digits(12345))
