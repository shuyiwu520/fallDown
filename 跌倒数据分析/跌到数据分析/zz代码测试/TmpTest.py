import xlwt
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
sheet.write(1,1,"python")
# 保存文件，默认为程序同级目录
wbk.save("test.xls")