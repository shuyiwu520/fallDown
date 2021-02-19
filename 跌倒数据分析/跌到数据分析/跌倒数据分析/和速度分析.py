import math
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook


xpix_data = []
x_data = []
wb = open_workbook('test_copy.xls')

for s in wb.sheets():
    # print('Sheet:', s.name)
    for row in range(1,s.nrows):
        #统计整数坐标，设计数据
        xpix_data.append(row)
        # print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        x_data.append(values[0])
plt.grid()

# 设置图像的尺寸大小
plt.figure(figsize=(8,2))

# 绘制x,y,z轴上的数据
plt.plot(xpix_data, x_data,label='x轴数据')

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#给图像添加坐标说明和图例说明
plt.title(u"日常数据波形")
plt.xlabel(u"数据时间先后序列")
plt.ylabel(u"数据波动值")
plt.legend()

# plt.savefig("C:/Users/wu/Desktop/国创养老系统/photo/x-y-z轴数据.png")
plt.show()
print("over!")