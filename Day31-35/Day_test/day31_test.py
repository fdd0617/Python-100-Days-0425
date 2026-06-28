# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }



# for key, value in prices.items():
#     if value > 100:
#         print(f"{key} {value}")

# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)
# # 用股票价格大于100元的股票构造一个新的字典
# # prices2 = {key: value for key, value in prices.items() if value > 100}
# # print(prices2)
# - 嵌套的列表的坑

# import openpyxl
# from pathlib import Path
# file_path = Path(__file__).parent / '考试成绩表A.xlsx'

# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))


# # 写入Excel
# wb = openpyxl.Workbook()

# sheet = wb.active
# sheet.title = '期末成绩'

# sheet.cell(1, 1, '姓名')  # A1单元格
# for col_index, course in enumerate(courses):
#     sheet.cell(1, col_index + 2, course)

# for row_index, name in enumerate(names):
#     sheet.cell(row_index + 2, 1, name)

#  #          ↑ 行（从第2行开始）  ↑ 列（从第2列开始）  ↑ 取出对应成绩
# for row_index, name in enumerate(names):
#     for col_index, course in enumerate(courses):
#         sheet.cell(row_index + 2, col_index + 2, scores[row_index][col_index])

# wb.save(file_path)



# import itertools

# # 产生ABCD的全排列
# itertools.permutations('ABCD')
# # 产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# # 产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))

# comp匿名函数：比较两个值，如果 x < y 返回 True，否则返回 False
# def select_sort(items, comp=lambda x, y: x < y):
#     # 复制列表，排序变动不影响原列表
#     items = items[:]
#     # 以列表索引循环遍历
#     for i in range(len(items) - 1):
#         # 设置最小值的索引
#         min_index = i
#         # 从第一个元素和后面的比较
#         for j in range(i + 1, len(items)):
#             # 调用匿名函数，更新最小值索引 # 比较items[j]和当前最小值，如果更小则更新最小值索引
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         # 调换位置，最小值放在前面
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# items = [5,3,6,8,2,1]
# res = select_sort(items)
# print(res)


  # 公鸡5元一只 母鸡3元一只 小鸡1元三只
  # 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只

# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(x,y,z)



  # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
  # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
  # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break

#     if enough:
#         print(fish)
#         break
#     fish += 5


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight
    
def input_thing():
    """输入商品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    """主函数"""
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))

    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_price += thing.price
            total_weight += thing.weight

    print(f'总价值: {total_price}美元')

if __name__ == '__main__':
    main()
