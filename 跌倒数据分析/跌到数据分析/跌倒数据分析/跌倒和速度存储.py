import math
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook
import xlwt


xpix_data = []
x_data = []
y_data = []
z_data = []
xyz_data = []
wb = open_workbook('../a测试数据集合/向前跌倒 - 副本.xlsx')

for s in wb.sheets():
    # print('Sheet:', s.name)
    for row in range(1,s.nrows):
        #统计整数坐标，设计数据
        xpix_data.append(row)
        # print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        # print(values[2])
        # print(values[0]*values[0] + values[1]*values[1]+ values[2] * values[2])
        x_data.append(values[0])
        y_data.append(values[1])
        z_data.append(values[2])
        # 计算三轴加速的a = x^2 + y^2 + z^2
        xyz_data.append(math.sqrt(values[0] * values[0] + values[1] * values[1] + values[2] * values[2]))

# 使用Workbook创建一个表格
wbk = xlwt.Workbook()
# add_sheet添加工作表
sheet = wbk.add_sheet("sheet")
# 对工作表进行操作 第一个数字代表行 从0开始 第二个数字代表列 从0开始
sheet.write(0,0,'合加速度')
for i in range(len(x_data)):
    sheet.write(i+1, 0, xyz_data[i])
    # 保存文件，默认为程序同级目录
wbk.save("test.xls")