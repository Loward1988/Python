import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# 作者：longanyang
# 使用说明
# 1.终端安装python3和pandas库
# 2.将下载的csv文件命名为grafana_data_export.csv并放在此py同目录下 终端执行'python3 script.py'
# 3.已做去空处理

df = pd.read_csv('./grafana_data_export.csv', skiprows=[0])  # 忽略第一行
rows = df.shape[0]
while rows > 0:
    rows -= 1
    a = df.values[rows-1]
    a = a[0].split(';')                     # 按分号分割字符串为数组
    df.values[rows-1] = a[2]                # 用分割字符数组的最后一个代替原df对应行的值
df.columns = ['A']                          # 起列名A
a = df['A']
rows = df.shape[0]
while rows > 0:                               # 字符转数字 为空的转为0
    rows -= 1
    if df.values[rows-1] != "null":
        df.values[rows-1] = float(df.values[rows-1])
    else:
        df.values[rows-1] = 0

df = df[df.A > 0]
arr = df['A']
arr = arr.values
arr = arr.tolist()


# 平均耗时
print('平均毫秒:%s' % round(np.mean(arr), 2))

# 中位数
print('中位数:%s' % round(np.median(arr), 2))

# 1s内占比
rows = df.shape[0]                  # 多少行
greater_df = df[df.A >= 1000]       # 取出大于1的
greater_rows = greater_df.shape[0]  # 行数
percents = 1 - round((greater_rows/rows), 4)
print('1s内占比:%s%%' % (str(percents*100)))

# 方差
print('方差：%s' % np.var(arr))
# 标准差
print('标准差：%s' % np.std(arr))
# 极差
print('极差：%s' % np.ptp(arr))
# 变异系数
print('变异系数：%s%%' % round((np.std(arr)/np.mean(arr)*100), 2))

# plt.plot(arr)