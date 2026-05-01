# # 生成一个随机验证码
# import string
# import random

# # 设置验证码格式：字母加数字
# all_chars = string.digits + string.ascii_letters

# def generate_code(code_len = 4):
#     return ''.join(random.choices(all_chars,k = code_len))


# for _ in range(5):
#     print(generate_code(6))


# 判断素数：

# def is_prime(num:int) -> bool:
#     """
    
#     """
#     for i in range(2,int(num ** 0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# res = is_prime(97)
# print(res)


# 最大公约数、最小公倍数

# def lcm(x:int,y:int):
#     return x*y//gcd(x,y)


# def gcd(x : int,y : int):
#     while y % x != 0:
#         x,y = y%x,x
#     return x
    

# res = lcm(16,99)
# print(res)

# 双色球随机选号：

# import random
# RED = '\033[31m'
# BLUE = '\033[34m'
# RESET = '\033[0m'

# red_balls = [i for i in range(1,34)]
# blue_balls = [i for i in range(1,17)]

# def choose():
#     selectd_balls = random.sample(red_balls,6)
#     selectd_balls.sort()
#     selectd_balls.append(random.choice(blue_balls))
#     return selectd_balls

# def display(balls):
#     for ball in balls[:-1]:
#         print(f"{RED}{ball:0>2d}{RESET}",end = ' ')
#     print(f"{BLUE}{balls[-1]:0>2d}{RESET}")

# n = int(input('生成几注号码？'))
# for _ in range(n):
#     display(choose())


# 生成制定长度的验证码

# import random
# import string

# all_chars = string.digits + string.ascii_letters


# def make_code(code_len = 4):
#     return ''.join(random.choices(all_chars,k=code_len))

# for _ in range(4):
#     print(make_code(6))



# def add(x,y):
#     return x+y

# def mul(x,y):
#     return x*y

# def cal(init_value,op_func,*args,**kwargs):
#     items = list(args) + list(kwargs.values())
#     result = init_value

#     for item in items:
#         if type(item) in (int,float):
#             result = op_func(result,item)

#     return result


# print(cal(3,add,1))


# def is_even(num):
#     return num % 2 == 0

# def square(num):
#     return num ** 2

# old_num = [35,2,4,6,8,9]
# new_num = list(map(square,filter(is_even,old_num)))
# new_nums = [num ** 2 for num in old_num if num % 2 == 0]
# new_nums2 = list(map(lambda x:x**2,filter(lambda x:x%2== 0,old_num)))
# print(new_nums2)
# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
# new_strings = sorted(old_strings,key=len)
# print(new_strings)
# print(old_strings)
# old_strings.sort(key=len)
# print(old_strings)

# import functools
# import operator

# fac = lambda n: functools.reduce(operator.mul,range(2,n+1),1)
# print(fac(6))

# def mull(nums):
#     res = 1
#     for i in range(1,nums+1):
#         res *= i

#     return res

# res1 = mull(6)
# print(res1)


# def is_prime(num):
#     for i in range(2,int((num**0.5)+1)):
#         if num % i == 0:
#             return False
#     return True

# is_prime1 = lambda x: all(map(lambda f: x%f,range(2,int(x**0.5)+1)))


# def is_prime2(num):
#     return num > 1 and all(num%f for f in range(2,int(num ** 0.5)+ 1))


# print(is_prime(67))
# print(is_prime1(67))
# print(is_prime2(67))


'''
day16练习
题目1：
    输出：12
    把一个函数知悉行两次
'''
# def apply(func,value):
#     return func(func(value))

# def double(x):
#     return x*2
# print(apply(double,3))

# '''
# 题目2：一个学生是成绩列表，按成绩高低排序，成绩相同的按照姓名字母排序

# '''
# students = [('Alice',85),('Bob',92),('Charlie',85),('David',92)]

# new_std = sorted(students,key=lambda x:(-x[1],x[0]))
# print(new_std)

# '''
# 题目3：十六进制转换整数
# '''

# import functools

# hex_to_int = functools.partial(int,base = 16)

# print(hex_to_int('ff'))

# students = [('Alice',85),('Bob',92),('Charlie',85),('David',92)]
# print(sorted(students,key=lambda x:x[0]))
# print(sorted(students,key=lambda x:x[1]))
# print(sorted(students,key=lambda x:x[1],reverse=True))
# print(sorted(students,key=lambda x:(-x[1],x[0])))
# print(sorted(students,key=lambda x:(x[1],x[0])))
# print(sorted(students,key=lambda x:(x[1],x[0]),reverse=True))
