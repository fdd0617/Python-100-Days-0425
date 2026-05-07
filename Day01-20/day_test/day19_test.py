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

# class GameCharacter:
#     def __init__(self,name,level,coins=0):
#         self.name = name
#         self.level = level
#         self.__coins = coins

#     def earn_coins(self,amount):
#         if amount <= 0 :
#             return 
#         self.__coins += amount

#     def spend_coins(self,amount):
#         if self.__coins < amount :
#             return 
#         if amount <= 0 :
#             return 
#         self.__coins -= amount

#     @property
#     def coins(self):
#         return self.__coins


# player = GameCharacter('Arthur', 5)
# player.earn_coins(100)
# player.spend_coins(30)
# print(player.coins)

# 练习 2：用户注册验证器

# 定义一个 User 类：

# 初始化时接收 username、password
# 用静态方法 is_valid_username(username) 判断用户名是否合法
# 用户名要求：长度 3 到 12，只能包含字母、数字、下划线
# 用静态方法 is_strong_password(password) 判断密码强度
# 密码要求：至少 8 位，同时包含字母和数字
# 只有用户名和密码都合法时才创建用户对象

# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password


#     @staticmethod
#     def is_valid_username(username):
#         if not 3 <= len(username) <= 12:
#             return False
#         for char in username:
#             if not (char.isalpha() or char.isdigit() or char == '_'):
#                 return False
        
#         return True
    
#     @staticmethod
#     def is_strong_password(password):
#         if len(password) < 8:
#             return False
#         has_alpha = False
#         has_digit = False

#         for char in password:
#             if char.isalpha():
#                 has_alpha = True
#             elif char.isdigit():
#                 has_digit = True

#         return has_alpha and has_digit

    

# if User.is_valid_username('jack_123') and User.is_strong_password('abc12345'):
#     user = User('jack_123','abc12345')
#     print("用户创建成功。")
# else:
#     print("用户名或密码不合法。")


# 练习 3：商品价格系统

# 定义一个 Product 类：

# 初始化时接收 name、price、discount
# price 使用私有属性 __price
# discount 表示折扣，例如 0.8 表示八折
# 用 @property 提供：
# price
# final_price
# final_price 返回折后价格
# 如果设置的价格小于等于 0，抛出提示或拒绝修改
# 进阶要求：
# 给 price 添加 setter：

# class Product:
#     def __init__(self,name,price,discount):
#         self.name = name
#         self.__price = price
#         self.discount = discount

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,value):
#         if value <= 0:
#             print(f"价格必须大于0")
#             return
#         self.__price = value
    

#     @property
#     def show_final_price(self):
#         if self.__price * self.discount > 0:
#             return self.__price * self.discount
#         else:
#             return f"价格不对"

# product =Product('apple',10,0.8)
# print(product.price)
# print(product.show_final_price)
# product.price = -5
# print(product.price)


# class Appconfig:
#     # 限定属性
#     __slots__ = ('host','port','debug',)


#     def __init__(self,host,port,debug):
#         self.host = host
#         self.port = port
#         self.debug = debug

# config = Appconfig('127.0.0.1',8000,'null')
# config.database = 'sql'


# 练习 5：文件大小单位转换器

# 定义一个 FileSize 类：

# 初始化时接收字节数 bytes_count
# 用静态方法 is_valid_size(value) 判断字节数是否合法，必须是非负整数
# 用 @property 提供：
# kb
# mb
# gb
# 分别返回对应单位的大小

# class FileSize:
#     def __init__(self,bytes_count):
#         self.bytes_count =bytes_count

#     @staticmethod
#     def is_valid_size(value):
#         if value > 0:
#             return value
        
#     @property
#     def kb(self):
#         return self.bytes_count / 1024


# 练习 6：银行账户体系

# 定义父类 BankAccount：
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance

#     # 父类的私有属性，子类无法直接访问
#     # 父类提供受控的方法属性，子类通过接口操作余额
#     @property
#     def balance(self):
#         return self.__balance
    
#     # balance属性是只读的，子类无法直接修改，父类需要提供一个专门的方法来啊修改余额，子类调用该方法
#     def _set_balance(self,value):
#         self.__balance = value

#     def deposit(self,amount):
#         if amount <= 0:
#             return f"请输入正确的金额。"
        
#         self.__balance += amount
#         return self.__balance
            
        

#     def withdraw(self,amount):
#         if amount <= 0:
#             return f"请输入正确的金额。"
        
#         if amount <= self.__balance:
#             self.__balance -= amount
#             return self.__balance
        
#         return f"余额不足。"
    




# # 属性：owner
# # 私有属性：__balance
# # 方法：
# # deposit(amount)
# # withdraw(amount)
# # balance 只读属性
# # 定义两个子类：

# # SavingsAccount 储蓄账户
# # 取款时不能透支
# # CreditAccount 信用账户
# # 初始化时增加 credit_limit
# # 允许透支，但不能超过信用额度
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance):
#         super().__init__(owner, balance)

# class CreditAccount(BankAccount):
#     def __init__(self, owner, balance,credit_limit):
#         super().__init__(owner, balance)
#         self.credit_limit = credit_limit

#     def withdraw(self,amount):
#         if amount <= 0:
#             return f"请输入正确的金额。"
#         # 信用账户验证余额的透支额度，self.balance可以访问父类的balance方法，返回balance属性
#         # 调用父类的_set_balaance方法，修改余额
#         if amount <= self.balance + self.credit_limit:
#             self._set_balance(self.balance - amount)
#             return self.balance
        
#         return f"信用额度不足。" 


# # 创建一个函数：

# # def process_withdraw(account, amount):
# #     account.withdraw(amount)
# # 分别传入储蓄账户和信用账户，观察行为不同。

# # 覆盖知识点：继承、私有属性、@property、方法重写、多态。
# def process_withdraw(account, amount):
#     res = account.withdraw(amount)
#     print(res)

# savings = SavingsAccount('张三',1000)
# credit = CreditAccount('李四',1000,500)
# process_withdraw(savings,1200)
# process_withdraw(credit,1200)

# print(savings.balance)
# print(credit.balance)



# 练习 7：通知系统

# 定义父类 Notifier：

# class Notifier:
#     def send(self, message):
#         pass
# # 定义三个子类：

# # EmailNotifier
# class EmailNotifier(Notifier):
#     def send(self,message):
#         return f"邮件通知：{message}"
# # SMSNotifier
# class SMSNotifier(Notifier):
#     def send(self,message):
#         return f"短信通知：{message}"
# # WechatNotifier
# class WechatNotifier(Notifier):
#     def send(self,message):
#         return f"微信通知：{message}"
# # 分别重写 send() 方法，输出不同格式：

# # 邮件通知：xxx
# # 短信通知：xxx
# # 微信通知：xxx
# # 然后创建列表：

# notifiers = [
#     EmailNotifier(),
#     SMSNotifier(),
#     WechatNotifier()
# ]
# # 遍历列表统一调用：

# for notifier in notifiers:
#     res = notifier.send('你的验证码是 123456')
#     print(res)
# # 覆盖知识点：继承、方法重写、多态。


# 练习 8：订单系统

# 定义一个 Order 类：
# class Order:
#     def __init__(self,order_id,items):
#         self.order_id = order_id
#         self.items = items

#     # @property作用是像属性一样访问方法  @property方法只能接收self
#     @property
#     def total_price(self):
#         total_price = 0
#         for item in self.items:
#             total_price += item['price'] * item['quantity']
        
#         return total_price
    
#     @staticmethod
#     def is_valid_item(items):
#         for item in items:
#             if item['price'] <= 0 and item['quantity'] <= 0:
#                 return False
#         return True

# items = [
#     {'name': '鼠标', 'price': 99, 'quantity': 2},
#     {'name': '键盘', 'price': 66, 'quantity': 1},
#     {'name': '显示器', 'price': 88, 'quantity': 2}
# ]


# if Order.is_valid_item(items):
#     current_order = Order(1,items)
#     res = current_order.total_price
#     print(res)
# else:
#     print(f"是商品不合法")

# 初始化时接收：
# order_id
# items
# items 是一个列表，每个元素是字典：
# {'name': '鼠标', 'price': 99, 'quantity': 2}
# 要求：

# 用 @property 实现 total_price
# 用静态方法 is_valid_item(item) 判断商品是否合法
# 商品必须包含 name、price、quantity
# price 和 quantity 都必须大于 0
# 创建订单前先验证所有商品是否合法
# 覆盖知识点：静态方法、@property、对象创建前验证。




# 练习 9：员工薪资系统

# 定义父类 Employee：

# 属性：name
# 方法：get_salary()

# class Employee:
#     def __init__(self,name):
#         self.name = name

#     def get_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self, name,salary):
#         super().__init__(name)
#         self.salary = salary

#     def get_salary(self):
#         return self.salary
    
# class PartTimeEmployee(Employee):
#     def __init__(self, name,salary,hour):
#         super().__init__(name)
#         self.salary = salary
#         self.hour = hour

#     def get_salary(self):
#         return self.salary * self.hour
    
# class SalesEmployee(Employee):
#     def __init__(self, name,base_salary,sale,qu):
#         super().__init__(name)
#         self.base_salary = base_salary
#         self.sale = sale
#         self.qu = qu

#     def get_salary(self):
#         return self.base_salary + (self.sale * self.qu)

# # 定义三个子类：

# # FullTimeEmployee
# # 固定月薪
# # PartTimeEmployee
# # 按小时工资和工作小时数计算工资
# # SalesEmployee
# # 底薪 + 销售额 * 提成比例
# # 创建一个员工列表，统一计算总工资：

# employees = [
#     FullTimeEmployee('张三', 10000),
#     PartTimeEmployee('李四', 80, 120),
#     SalesEmployee('王五', 5000, 20000, 0.1)
# ]

# total = 0
# for emp in employees:
#     salary = emp.get_salary()
#     total += salary
#     print(f"{emp.name}工资{salary}")
# # 覆盖知识点：继承、方法重写、多态。




# 练习 10：从字符串创建对象

# 定义一个 Date 类：
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day

    
#     @property
#     def iso_format(self):
#         return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

#     @staticmethod
#     def is_valid_date(year, month, day):
#         if year <= 0:
#             return False
#         if not 0 < month <= 12:
#             return False
#         if not 0 < day <= 31:
#             return False
        
#         return True
    
#     @classmethod
#     def from_string(cls, date_str):
#         # 按照‘-‘符号分割，返回一个列表['2026', '05', '04']

#         parts = date_str.split('-')

#         if len(parts) != 3:
#             return None
#         # 列表中的三个字段分别取出来 赋值
#         year_str, month_str, day_str = parts

#         # 赋值后，用方法判定是否是数字组成
#         if not year_str.isdigit():
#             return None
#         if not month_str.isdigit():
#             return None
#         if not day_str.isdigit():
#             return None
        

#         # 转换成整数  要判断比较
#         year = int(year_str)
#         month = int(month_str)
#         day = int(day_str)

#         # 调用方法判断是否合法 类方法 cls 就代表当前类 Date。 
#         if not cls.is_valid_date(year, month, day):
#             return None
#         # 最后创建对象并返回
#         return cls(year, month, day)



# d = Date.from_string('2026-05-04')

# if d is not None:
#     print(d.iso_format)
# else:
#     print('日期不合法')

# 初始化时接收 year、month、day
# 用静态方法 is_valid_date(year, month, day) 简单判断日期是否合法
# 用类方法 from_string(cls, date_str) 从字符串创建对象
# 示例：

# d = Date.from_string('2026-05-04')
# 要求：

# 字符串格式必须是 YYYY-MM-DD
# 如果日期合法，返回 Date 对象
# 否则返回 None
# 用 @property 提供 iso_format，返回 '2026-05-04'


