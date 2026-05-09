"""
> **要求**：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
其中，部门经理的月薪是固定 15000 元；
程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。

1、定义一个父类 Employee ，三类员工继承该父类
部门经理 Manager salary = 15000
程序员 Programmer 增加属性 work_hour, 200
销售员 Salesman 增加属性 sales 

from abc import ABCMeta, abstractmethod
定义抽象类 抽象方法 作用是子类必须实现父类中的方法
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """获取工资"""
        pass


class Manager(Employee):
    """部门经理"""
    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 15000.0
    

class Programmer(Employee):
    """程序员"""
    def __init__(self, name, work_hour=0):
        super().__init__(name)
        self.work_hour = work_hour

    def get_salary(self):
        return self.work_hour * 200
    

class Salesman(Employee):
    """销售"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05
    

# 修改工资系统，增加一种员工类型 HourlyWorker，时薪和工时都由用户输入。
# 不用 isinstance，还能不能完成工资结算？想一想为什么。

class HourlyWorker(Employee):
    def __init__(self, name,work_hour=0,salary=0):
        super().__init__(name)
        self.work_hour = work_hour
        self.salry = salary

    def get_salary(self):
        return self.work_hour * self.salry


emps = [Manager('刘备'), HourlyWorker('范斗斗'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]

for emp in emps:
    if isinstance(emp, Programmer):
        emp.work_hour = int(input(f"请输入{emp.name}本月工作时间: "))

    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额: '))

    elif isinstance(emp, HourlyWorker):
        emp.work_hour = int(input(f"请输入{emp.name}本月工作时间: "))
        emp.salry = float(input(f'请输入{emp.name}时薪: '))

    print(f"{emp.name}本月工资为：¥{emp.get_salary():.2f}元")