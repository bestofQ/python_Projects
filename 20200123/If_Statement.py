"""
time:2020.01.23
"""
'''
布尔型
true false
'''
print('布尔型')
w = True
m = False
if w:
    print('布尔型 true')
if m:
    print('布尔型 false')
'''
比较运算符：>、<、==、!=、>=、<=
'''
print('比较运算符')
print(1 <= 1)
print('a' == 'A')
'''
if else
'''
import random
some_num = random.randint(1, 100)
if some_num % 2 == 1:
    print(str(some_num) + '是奇数')
else:
    print(str(some_num) + '是偶数')