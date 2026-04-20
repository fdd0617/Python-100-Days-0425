# 通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中
# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = input("请输入成绩：")
#         temp.append(score)
#     scores.append(temp)
# print(scores)
# 通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中
# import random
#
# scores = [[random.randrange(60,101) for _ in range(3)] for _ in range(5)]
# print(scores)
# 双色球
import random

from rich.console import Console
from rich.table import Table

# red_balls = list(range(1,34))
# current_balls = []
# for _ in range(6):
#     index = random.randrange(len(red_balls))
#     current_balls.append(red_balls.pop(index))
#
# current_balls.sort()
# for ball in current_balls:
#     print(f"\033[031m{ball:0>2d}\033[0m",end = ' ')
# blue_balls = random.randrange(1,17)
# print(f'\033[034m{blue_balls:0>2d}\033[0m')

# n = int(input("生成几注？"))
# red_balls = [i for i in range(1,34)]
# blu_balls = [i for i in range(1,17)]
# for _ in range(n):
#     select_balls = random.sample(red_balls,6)
#     select_balls.sort()
#     for ball in select_balls:
#         print(f"\033[031m{ball:0>2d}\033[0m",end = ' ')
#     blue_balls = random.choice(blu_balls)
#     print(f'\033[034m{blue_balls:0>2d}\033[0m')


console = Console()

n = int(input("生成几注？"))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

table = Table(show_header=True)
for col_name in ('序号','红球','蓝球','最终'):
    table.add_column(col_name,justify='center')

for i in range(n):
    current_ball = random.sample(red_balls,6)
    current_ball.sort()
    blue_ball = random.choice(blue_balls)

    table.add_row(
        str(i+1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in current_ball])}[/red]',
        # f'{" ".join([f"{ball:0>2d}" for ball in current_ball])}',
        f'[blue]{blue_ball:0>2d}[/blue]',
        f'[red]{" ".join([f"{ball:0>2d}" for ball in current_ball])}[/red] [blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)