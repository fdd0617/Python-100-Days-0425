# # class Student:
# #     # __slots__ = ('name','age')

# #     def __init__(self,name,age):
# #         self.__name = name
# #         self.__age = age


# #     def study(self,course):
# #         print(f"{self.__name}正在学习{course}")

# #     @staticmethod
# #     def show(name):
# #         print({name})

# # stu = Student('王大锤',20)
# # # stu.sex = '男'
# # stu.study('python')
# # print(stu._Student__name)
# # # print(stu.sex)


# # Student.show('python')


# class Triangle(object):

#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     @staticmethod
#     def is_valid(a,b,c):
#         return a + b > c and b + c > a and a + c > b
    
#     @property
#     def perimeter(self):
#         return self.a + self.b + self.c

#     @property
#     def area(self):
#         p = self.perimeter / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5



# if Triangle.is_valid(3,2,5):
#     t = Triangle(3,4,5)
#     print(f"周长：{t.perimeter}")
#     print(f"面积：{t.area}")
# else:
#     print('无效的边长。')




# 继承
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f"{self.name}正在吃饭")

#     def sleep(self):
#         print(f"{self.name}正在睡觉。")




# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def study(self,course_name):
#         print(f"{self.name}正在学习{course_name}")


# class Teacher(Person):
#     def __init__(self, name, age,title):
#         super().__init__(name, age)
#         self.title= title

#     def teach(self,course_name):
#         print(f"{self.name}{self.title}正在讲授{course_name}")


# stu1 = Student('李元芳',21)
# stu2 = Student('狄仁杰',22)
# tea1 = Teacher('武则天',35,'副教授')

# stu1.eat()
# stu2.sleep()
# tea1.eat()
# stu1.study('Python')
# tea1.teach('Python')
# stu2.study('科学')


# 练习 1：属性可见性

# 定义一个 Student 类：

# 初始化时接收 name 和 age
# 将 name 设置为私有属性 __name
# 定义 study(course_name) 方法，输出：某某正在学习某课程
# 尝试在类外部访问 stu.__name，观察报错
# 再尝试用 _Student__name 访问它
# 思考：Python 的“私有属性”是真的完全无法访问吗？

# class Student:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age

#     def study(self,course_name):
#         print(f"{self.__name}正在学习。")


# stu1 = Student('张三',20)
# stu1.study('python')
# # print(stu1.__name)
# print(stu1._Student__name)


# 练习 2：动态属性

# 定义一个 Book 类，初始化时包含：

# title
# author
# 创建一个 Book 对象后，动态添加一个属性：

# book.price = 59.9
# 然后输出 book.title、book.author、book.price。

# 思考：为什么 Python 可以在对象创建后继续添加属性？ 动态语言


# class Book:
#     __slots__ = ('title', 'author')


#     def __init__(self,title,author):
#         self.title = title
#         self.author = author

    
# book1 = Book('Python程序设计','Python')
# book1.price = 59.9

# print(book1.title)
# print(book1.author)
# print(book1.price)

# 思考：__slots__ 的作用是什么？ 限定类的属性，不能再外部添加


# 练习 4：静态方法

# 定义一个 Triangle 类：

# 初始化时接收三条边 a、b、c
# 定义静态方法 is_valid(a, b, c)，判断三条边能否构成三角形
# 如果三条边有效，就创建三角形对象
# 如果无效，输出：无效的边长


# class Triangle:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     @staticmethod
#     def is_valid(a,b,c):
#         return a + b > c and b + c > a and a + c > b
    
#     @property
#     def perimeter(self):
#         return self.a + self.b + self.c

#     @property
#     def area(self):
#         p = self.perimeter / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# if Triangle.is_valid(1,2,3):
#     t = Triangle(1,2,3)
#     print(t.perimeter)
#     print(t.area)

# else:
#     print('无效的边长')


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f"{self.name}正在吃饭。")

#     def sleep(self):
#         print(f"{self.name}正在睡觉。")

#     def introduce(self):
#         pass

#     def show_info(person):
#         person.introduce()




# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def study(self,course_name):
#         print(f"{self.name}正在学习{course_name}")

#     def introduce(self):
#         print(f"我是学生{self.name},今年{self.age}")


# class Teacher(Person):
#     def __init__(self, name, age,title):
#         super().__init__(name, age)
#         self.title = title

#     def teach(self,course_name):
#         print(f"{self.name}正在讲授{course_name}")

#     def introduce(self):
#         print(f"我是{self.name},职称是{self.title}")


# stu1 = Student('张三',18)
# stu2 = Student('李四',19)
# stu1.eat()
# stu2.sleep()
# tea1 = Teacher('刘老师',35,'一级教师')
# stu1.study('python')
# tea1.teach('python')
# stu1.introduce()
# tea1.introduce()
# stu1.show_info()
# tea1.show_info()



# 设计一个简单的校园人员管理程序：

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @property
#     def show_info(self):
#         return f"{self.name},{self.age}"

#     def introduce(self):
#         pass


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def study(self,course_name):
#         print(f"{self.name}正在学习{course_name}")

#     def introduce(self):
#         print(f"我是学生{self.name},今年{self.age}")


# class Teacher(Person):
#     def __init__(self, name, age,title):
#         super().__init__(name, age)
#         self.title = title

#     def teach(self,course_name):
#         print(f"{self.name}正在讲授{course_name}")

#     def introduce(self):
#         print(f"我是{self.name},职称是{self.title}")


# people = [
#     Student('张三',18),
#     Student('李四',19),
#     Teacher('刘',35,'一级教师')
# ]

# for person in people:
#     print(person.show_info)

#     person.introduce


# **Day 19 练习题**

# **题目1（属性可见性）：** 下面代码的输出是什么？请解释原因。
# owner可以正常输出，balance不能输出，他是私有化属性
# ```python
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

# acc = Account('张三', 1000)
# print(acc.owner)
# print(acc.__balance)


# **题目2（静态方法 + @property）：** 请定义一个 `Circle` 类，包含：
# - 初始化方法接收半径 `radius`
# - 一个静态方法 `is_valid(r)` 判断半径是否大于 0
# - `area` 和 `circumference`（周长）用 `@property` 装饰器实现
# - 编写测试代码：先验证半径 5 是否合法，合法则创建对象并打印面积和周长
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     @staticmethod
#     def is_valid(r):
#         return r > 0
    
#     @property
#     def area(self):
#         return math.pi * (self.radius**2)
    
#     @property
#     def circumference(self):
#         return math.pi * self.radius * 2
    

# if Circle.is_valid(5):
#     t = Circle(5)
#     print(t.area)
#     print(t.circumference)
# else:
#     print('半径不对')


# # **题目3（继承）：** 已知父类如下：


# # ```

# # 请定义子类 `Dog` 和 `Cat`：
# # - `Dog` 继承 `Animal`，额外有一个 `fetch(item)` 方法，输出 `{name}去捡{item}`
# # - `Cat` 继承 `Animal`，重写 `speak()` 方法，输出格式为 `喵~我是{self.name}`（注意不使用 `self.sound`）
# # - 创建一个 `Dog('旺财', '汪')` 和一个 `Cat('咪咪', '喵')`，分别调用 `speak()` 和各自的特有方法，展示多态效果
# # ```python
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def speak(self):
#         print(f'{self.name}: {self.sound}!')

# class Dog(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name, sound)

#     def fetch(self,item):
#         print(f"{self.name}去捡{item}")

# class Cat(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name, sound)

#     def speak(self):
#         print(f"喵~我是{self.name}")


# dog = Dog('旺财', '汪')
# cat = Cat('咪咪', '喵')
# dog.speak()
# cat.speak()


# 练习 1：游戏角色背包系统

# 定义一个 GameCharacter 类：

# 初始化时接收 name、level
# 用私有属性保存金币数量：__coins
# 提供 earn_coins(amount) 方法增加金币
# 提供 spend_coins(amount) 方法消费金币
# 金币不能为负数
# 用 @property 提供只读属性 coins
# 要求：


# 思考：为什么金币适合做成私有属性？

class GameCharacter:
    def __init__(self,name,level,coins=0):
        self.name = name
        self.level = level
        self.__coins = coins

    def earn_coins(self,amount):
        if amount <= 0 :
            return 
        self.__coins += amount

    def spend_coins(self,amount):
        if self.__coins < amount :
            return 
        if amount <= 0 :
            return 
        self.__coins -= amount

    @property
    def coins(self):
        return self.__coins


player = GameCharacter('Arthur', 5)
player.earn_coins(100)
player.spend_coins(30)
print(player.coins)