# import csv
# import random
# from pathlib import Path

# file_path = Path(__file__).parent / 'scores.csv'

# with open(file_path, 'w') as file:
#     writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']

#     for name in names:
#         scores = [random.randrange(50, 101) for _ in range(3)]
#         scores.insert(0, name)
#         writer.writerow(scores)


# import csv 
# from pathlib import Path

# file_path = Path(__file__).parent / 'scores.csv'

# with open(file_path, 'r') as file:
#     reader = csv.reader(file, delimiter= '|')
    # for data_list in reader:
    #     print(reader.line_num, end='\t')
    #     for elem in data_list:
    #         print(elem, end='\t')
    #     print()

# **Day 23 练习题 (3道):**

# **题目1: 学生成绩写入CSV**

# 编写程序, 将以下学生成绩数据写入students_scores.csv文件:
# - 张三: 语文85, 数学92, 英语78
# - 李四: 语文76, 数学88, 英语95
# - 王五: 语文90, 数学70, 英语85
# - 赵六: 语文88, 数学95, 英语92
# - 周七: 语文72, 数学83, 英语88

# 要求: 第一行为表头(姓名, 语文, 数学, 英语), 之后每行一个学生的数据。

import csv
from pathlib import Path

file_path = Path(__file__).parent / 'students_scores.csv'
with open(file_path, 'w', encoding='utf-8', newline='') as file:
    write = csv.writer(file)
    write.writerow(['姓名', '语文', '数学', '英语'])
    write.writerow(['张三', 85, 92, 78])
    write.writerow(['李四', 76, 88, 95])
    write.writerow(['王五', 90, 70, 85])
    write.writerow(['赵六', 88, 95, 92])
    write.writerow(['周七', 72, 83, 88])



# **题目2: 从CSV读取并统计**

# 编写程序, 读取题目1生成的students_scores.csv文件, 计算并打印:
# (a) 每个学生的平均分
# (b) 每门课程的平均分
# (c) 总分最高的学生姓名和分数

# 输出示例:

# ```
# 张三 平均分: 85.00
# 李四 平均分: 86.33
# ...
# 语文平均分: 82.20
# 数学平均分: 85.60
# ...
# 总分最高: 李四 259
# # ```
import csv 
from pathlib import Path


chinese_total = 0
math_total = 0
english_total = 0
student_count = 0

max_name = ''
max_total = 0


file_path = Path(__file__).parent / 'students_scores.csv'
with open(file_path, 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file)

    # 读取下一行， 常用于跳过表头
    header = next(reader)
    for row in reader:
        # print(row[0])
        name = row[0]
        Chinese = int(row[1])
        Math = int(row[2])
        English = int(row[3])

        total = Chinese + Math + English
        avg = total / 3
        print(f"{name}平均分：{avg:.2f}")

        chinese_total += Chinese
        math_total += Math
        english_total += English
        student_count += 1

        # 总分最高
        if total > max_total:
            max_total = total
            max_name = name


print(f'语文平均分: {chinese_total / student_count:.2f}')
print(f'数学平均分: {math_total / student_count:.2f}')
print(f'英语平均分: {english_total / student_count:.2f}')
print(f'总分最高: {max_name} {max_total}')

# **题目3: CSV数据筛选与导出**

# 编写程序, 读取students_scores.csv, 将平均分大于等于85分的学生筛选出来, 写入一个新的CSV文件good_students.csv, 并在最后新增一列"平均分"。

# 预期good_students.csv内容:

# ```
# 姓名,语文,数学,英语,平均分
# 李四,76,88,95,86.33
# 赵六,88,95,92,91.67
# ```

import csv 
from pathlib import Path



file_path = Path(__file__).parent / 'students_scores.csv'
file_path2 = Path(__file__).parent / 'good_students.csv'
with open(file_path, 'r', encoding='utf-8', newline='') as read_file:
    with open(file_path2, 'w', encoding='utf-8', newline='') as write_file:
        reader = csv.reader(read_file)
        write = csv.writer(write_file)

        header = next(reader)
        write.writerow(['姓名', '语文', '数学', '英语', '平均分'])

        for row in reader:
            # print(row)
            name = row[0]
            chinese = int(row[1])
            math = int(row[2])
            english = int(row[3])

            total = chinese + math + english
            avg = total / 3

            if avg >= 85:
                # print(row)
                write.writerow([name, chinese, math, english, f'{avg:.2f}'])
