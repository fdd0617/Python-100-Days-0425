"""
四、练习题（由浅到深）

基础题

什么是类，什么是对象？请分别举一个例子。
答：类是把一批对象的相同特征抽出来作为类。
    对象就是类的实例化，实际应用。
属性和方法有什么区别？
属性是表示对象有什么，方法表示对象能做什么

is-a 和 has-a 分别是什么意思？请各举一个例子。
is-a 是一个 是继承关系，student继承Person类的属性；
has-a 有一个 是组合、关联，student和teacher类有关联。student和book 学生有一个本书
为什么花色适合用 Enum，不适合直接用数字？
可读性好，方便维护。
理解题

在扑克案例中，Card、Poker、Player 各自负责什么？
Card负责定义牌的花色和点数，负责表示一张牌，保存一张牌的花色和点数。
Poker定义一副完整的扑克牌，创建洗牌、发牌动作。负责创建完整的52张牌，提供整副牌有关的操作，洗牌发牌
Player定义玩家， 负责表示一个玩家，保存玩家的姓名，以及玩家手里的牌，并提供玩家相关操作，摸牌，整理牌，显示手牌
为什么 Player.arrange() 之前，Card 需要实现 __lt__？
__lt__表示对象排序，告诉程序排序方式
__lt__ 用来定义 Card 对象之间“小于”的比较规则。因为 Player.arrange() 要对手牌排序，而手牌里是 Card 对象，Python 不知道如何比较它们，所以 Card 需要先实现 __lt__，告诉程序排序方式。

__repr__ 方法的作用是什么？
__repr__方法用来定义输出格式
工资结算案例中，为什么 Employee 适合做父类？
代码填空题

补全学生类：
class Student:
    def __init__(self, name, score):
        self.____ = name
        self.____ = score

    def show(self):
        print(f'{self.name}: {self.score}')
补全员工父类：
from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @____________
    def get_salary(self):
        pass
补全程序员类：
class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.____________ = working_hour

    def get_salary(self):
        return 200 * self.____________
编程题

写一个 Dog 类，有名字和年龄两个属性，有一个 bark() 方法输出“旺旺”。
写一个 Rectangle 类，有长和宽两个属性，提供计算周长和面积的方法。
写一个 Student 类，包含姓名和成绩，写一个方法判断是否及格。
写一个 Animal 父类，再写 Cat 和 Dog 子类，分别重写 make_sound() 方法。
仿照工资结算系统，再设计一个“交通工具”例子：
父类 Vehicle
子类 Car、Bike
都有 run() 方法，但输出不同内容
提升题

修改扑克牌案例，让玩家可以“摸一张牌”和“显示所有手牌”。
修改工资系统，增加一种员工类型 HourlyWorker，时薪和工时都由用户输入。
不用 isinstance，还能不能完成工资结算？想一想为什么。
五、如果你想真正学会，这样练最有效
你可以按这个节奏走：

先手写一个最简单的类，如 Student
再练一个 has-a 关系，如 ClassRoom 里有多个 Student
再练继承，如 Animal -> Dog/Cat
最后回来看工资结算系统，你会轻松很多

"""

# 写一个 Dog 类，有名字和年龄两个属性，有一个 bark() 方法输出“旺旺”。
# class Dog():
#     """定义dog类"""
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         return f"{self.name}：'旺旺'"
    

# dog = Dog('旺财',2)
# print(dog.bark())

# 写一个 Rectangle 类，有长和宽两个属性，提供计算周长和面积的方法。
# class Rectangle():
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     @property
#     def perimeter(self):
#         return (self.length + self.width) * 2
    
#     @property
#     def area(self):
#         return self.length * self.width
    

# res = Rectangle(3,5)
# print(res.perimeter)
# print(res.area)


# 写一个 Student 类，包含姓名和成绩，写一个方法判断是否及格。

# class Student():
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade

#     # 判断是否及格
#     def is_pass(self):
#         return self.grade >= 60
    
#     # 调用is_pass方法，输出结果
#     def show_result(self):
#         if self.is_pass():
#             print(f"{self.name}你及格了。")
#         else:
#             print(f"{self.name},你要继续努力。")

# std1 = Student('张三',89)
# std2 = Student('李四',59)
# std1.show_result()
# std2.show_result()


# 写一个 Animal 父类，再写 Cat 和 Dog 子类，分别重写 make_sound() 方法。

# from abc import ABCMeta,abstractmethod

# class Animal(metaclass=ABCMeta):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @abstractmethod
#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def make_sound(self):
#         return f"{self.name}会喵喵喵～"
    
# class Dog(Animal):
#     # 子类没有写__init__方法时，会自动继承父类的
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def make_sound(self):
#         return f"{self.name}会汪汪汪～"
    
# pets = [Cat('咪咪',2),Dog('旺财',1)]

# # 不同对象调用一个方法，表现出不同结果，这就是多态
# for pet in pets:
#     print(pet.make_sound())

# 仿照工资结算系统，再设计一个“交通工具”例子：
# 父类 Vehicle
# 子类 Car、Bike
# 都有 run() 方法，但输出不同内容


# from abc import ABCMeta,abstractmethod
# class Vehicle(metaclass=ABCMeta):
#     """交通工具 属性：brand品牌"""
#     def __init__(self,brand):
#         self.brand = brand

#     @abstractmethod
#     def run(self):
#         pass

# class Car(Vehicle):
#     def run(self):
#         return f"The man drives a {self.brand} car."
    
# class Bike(Vehicle):
#     def run(self):
#         return f"The man rides a {self.brand} bike."
    
# vehicles = [Car('BMW'),Bike('Trek')]
# for vehicle in vehicles:
#     print(vehicle.run())