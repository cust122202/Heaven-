'''
用最小二乘法求解
现给出几个离散点，求拟合函数。
步骤：
1.输入离散点的坐标值。
2.设计拟合函数y=ax+b.
3.根据已知离散点的x值，通过y=ax+b算出对应的y值。
4.将y值与离散点对应的y值做减法，然后求平方，即(yi-y^)^2
5.求最小值，对应可以得出ab的值。
6.根据拟合函数，给出新设想的x值，预测出对应的y值。

'''

import numpy as np
import matplotlib.pyplot as plt

#定义x、y散点坐标
x = [10,20,30,40,50,60,70,80]
x = np.array(x)
print('x is :\n',x)
num = [174,236,305,334,349,351,342,323]
y = np.array(num)
print('y is :\n',y)
#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
print('f1 is :\n',f1)

p1 = np.poly1d(f1)
print('p1 is :\n',p1)

#也可使用yvals=np.polyval(f1, x)
yvals = p1(x) #拟合y值
print('yvals is :\n',yvals)
#绘图
plot1 = plt.plot(x, y, 's',label='original values')
plot2 = plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4) #指定legend的位置右下角
plt.title('polyfitting')
plt.show()
