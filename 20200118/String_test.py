"""
time:2010.01.20
"""
# RMB转换美元
print('请输入要转换的金额(人民币):')
RMB = input()
USD = float(RMB) * 0.1589

print(f'{RMB}人民币等于{USD:.2f}美元')