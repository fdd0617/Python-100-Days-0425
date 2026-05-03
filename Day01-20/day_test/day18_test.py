# class Student:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def study(self,course_name):
#         print(f"学生{self.name}正在学习{course_name}。")
    
#     def play(self,game_name):
#         print(f"学生{self.name}正在玩{game_name}游戏。")


# std1= Student('Tom',18)
# print(std1)
# std = Student('jack',17)
# std.study('语文')
# std1.play('跳绳')


#### 例子1：时钟

# > **要求**：定义一个类描述数字时钟，提供走字和显示时间的功能。
# import time


# class Clock:
#     """模拟时钟"""
#     def __init__(self,hour=0,minute=0,second=0):
#         """
#         初始化方法：时分秒
#         """
#         self.hour = hour
#         self.min = minute
#         self.sec = second

#     def run(self):
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.min += 1
#             if self.min == 60:
#                 self.min = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
    
#     def show(self):
#         return f"{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}"
    

# clock = Clock(00,59,58)
# while True:
#     # 给时钟对象发消息读取时间
#     print(clock.show())
#     # 休眠一秒钟
#     time.sleep(1)
#     # 给时钟对象发消息，前进一秒钟
#     clock.run()


#### 例子2：平面上的点

# >  **要求**：定义一个类描述平面上的点，提供计算到另一个点距离的方法。

# class Point:
#     """平面上的点"""
#     def __init__(self,x=0,y=0):
#         """
#         初始化方法：坐标默认原点0，0
#         """
        
#         self.x,self.y = x,y

#     def distance_to(self,other):
#         """
#         计算与另一个点的距离
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return (dx**2 + dy**2)**0.5
    
#     def __str__(self):
#         return f"{self.x}, {self.y}"

    
# p1 = Point(3,5)
# p2 = Point(6,9)
# print(p1)
# print(p2)
# print(p1.distance_to(p2))

"""
题目 1：学生类

定义一个 Student 类。

要求：

有 name 和 age 两个属性。
有 study(course) 方法，输出：张三正在学习Python。
有 play() 方法，输出：张三正在玩游戏。
创建两个学生对象并调用方法。

"""
# class Student:
#     """创建一个学生类
#     """
#     def __init__(self,name,age):
#         """初始化属性
#         """
#         self.name = name
#         self.age = age

#     def study(self,course):
#         print(f"{self.name}正在学习{course}。")


#     def play(self):
#         print(f"{self.name}正在玩游戏。")

    
# std1 = Student('张三',18)
# std2 = Student('李四',17)
# std1.study('Python')
# std2.play()


# 题目 2：银行卡类

# 定义一个 BankAccount 类。

# 要求：

# 有 owner 和 balance 两个属性。
# 有 deposit(amount) 方法，用来存钱。
# 有 withdraw(amount) 方法，用来取钱。
# 如果余额不足，输出：余额不足。
# 有 show_balance() 方法，显示当前余额。


class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        """存钱
        """
        if amount <= 0:
            print("存款金额必须大于0。")
            return self.balance
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        """取钱
        """
        if amount > self.balance:
            print("余额不足")
            return self.balance
        self.balance -= amount
        return self.balance
    
    def show_balance(self):
        print(f"当前账户{self.owner}余额{self.balance}")


# account = BankAccount("小明", 1000)
# account.show_balance()
# account.deposit(500)
# account.show_balance()
# account.withdraw(300)
# account.show_balance()

# 题目 3：矩形类

# 定义一个 Rectangle 类。

# 要求：

# 有 width 和 height 两个属性。
# 有 area() 方法，返回面积。
# 有 perimeter() 方法，返回周长。
# 创建一个矩形对象，输出它的面积和周长。

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return (self.width + self.height)*2

# rect = Rectangle(10, 5)
# print(rect.area())       # 50
# print(rect.perimeter())  # 30

# 题目 4：计数器类

# 定义一个 Counter 类。

# 要求：

# 初始值默认为 0。
# 有 increase() 方法，每次让计数器加 1。
# 有 decrease() 方法，每次让计数器减 1。
# 有 show() 方法，返回当前计数。

# class Counter:
#     def __init__(self,count=0):
#         self.count = count

#     def increase(self):
#         self.count += 1
#         return self.count
    
#     def decrease(self):
#         self.count -= 1
#         return self.count
    
#     def show(self):
#         return self.count
    

# counter = Counter()
# counter.increase()
# counter.increase()
# counter.decrease()
# print(counter.show())    # 1


# 题目 5：改进 Clock 类

# 在你现在的 Clock 类基础上增加功能。

# 要求：

# 增加 set_time(hour, minute, second) 方法，用来重新设置时间。
# 增加 is_midnight() 方法，判断当前时间是不是 00:00:00。
# 如果是午夜，返回 True，否则返回 False。

class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    
    def show(self):
        return f"{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}"
    
    def set_time(self,hour, minute, second):
        self.hour = hour
        self.min = minute
        self.sec = second


    def is_midnight(self):
        if self.hour == 0 and self.min == 0 and self.sec == 0:
            return True
        return False
    


clock = Clock(23, 59, 59)
clock.run()
print(clock.show())          # 00:00:00
print(clock.is_midnight())   # True
clock.set_time(1,1,1)
print(clock.show())  