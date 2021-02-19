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
wb = open_workbook('../a测试数据集合/accelerationData_copy.xlsx')

for s in wb.sheets():
    # print('Sheet:', s.name)
    # 从第2行开始遍历数据
    for row in range(1,s.nrows):
        #统计整数坐标，设计数据
        xpix_data.append(row)
        # print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        x_data.append(values[0])
        y_data.append(values[1])
        z_data.append(values[2])
        # 计算三轴加速的a = x^2 + y^2 + z^2
        xyz_data.append(math.sqrt(values[0] * values[0] + values[1] * values[1] + values[2] * values[2]))
# 使用Workbook创建一个表格
wbk = xlwt.Workbook()
# add_sheet添加工作表
sheet = wbk.add_sheet("sheet")
# 设置样式，初始化样式
style = xlwt.XFStyle()
#设置字体
font = xlwt.Font()
font.name = u"微软雅黑"
font.colour_index = 4
font.bold = True
style.font = font
# 对工作表进行操作 第一个数字代表行 从0开始 第二个数字代表列 从0开始
sheet.write(0,1,'hello',style)
for i in range(len(x_data)):
    sheet.write(i+1, 1, xyz_data[i])
    # 保存文件，默认为程序同级目录
wbk.save("test.xls")
