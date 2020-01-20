"""
time:2020.01.19
"""
# 将你的名字赋予给变量name，将你的出生年份赋予给变量birth_year
# 分别使用F-Strings和str.format()的方法打印出你的年龄
# 例如 “小明,你今年18岁了”
# F-Strings
age = 18.0
print(f'小明,你今年{int(age)}岁了')
# str.format()
print('小明,你今年{}岁了'.format(age))