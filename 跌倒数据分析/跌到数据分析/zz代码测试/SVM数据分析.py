import numpy as np
import pylab as pl   #画图用
from sklearn import svm

#随机生成两组二位数据
np.random.seed(0)#使每次产生随机数不变
X = np.r_[np.random.randn(20,2)-[2,2],np.random.randn(20,2)+[2,2]]#注意这里np.r_[],而不是np.r_（）我都打错了，会报错TypeError: 'RClass' object is not callable
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等

Y = [0] * 20+[1] * 20#Python原来可以这么简单的创建重复的列表呀

clf=svm.SVC(kernel='linear')
clf.fit(X,Y)

w=clf.coef_[0]
a=-w[0]/w[1]
xx=np.linspace(-5,5)#产生-5到5的线性连续值，间隔为1
yy=a*xx-(clf.intercept_[0])/w[1]  #clf.intercept_[0]是w3.即为公式a1*x1+a2*x2+w3中的w3。(clf.intercept_[0])/w[1]即为直线的截距

#得出支持向量的方程
b=clf.support_vectors_[0]
yy_down=a*xx+(b[1]-a*b[0])#(b[1]-a*b[0])就是简单的算截距
b=clf.support_vectors_[-1]
yy_up=a*xx+(b[1]-a*b[0])

print("w:",w) #打印出权重系数
print("a:",a) #打印出斜率
print("suport_vectors_:",clf.support_vectors_)#打印出支持向量
print("clf.coef_:",clf.coef_)                  #打印出权重系数，还是w


#这个就是画出来而已。很简单，也不太常用，都用matplotlib去了。不多说了
pl.plot(xx,yy,'k-')
pl.plot(xx,yy_down,'k--')
pl.plot(xx,yy_up,'k--')

pl.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,0],s=80,facecolors='none')
pl.scatter(X[:,0],X[:,1],c=Y,cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()