import numpy as np


i2 = np.eye(2)
print(i2)
np.savetxt('eye.txt',i2)

c,v = np.loadtxt('data.csv',delimiter=',',usecols=(1,2),unpack=True)
print(c,v)
wap = np.average(c,weights=v)#加权平均值
print(wap)
ave = np.mean(c)#算数平均值
print(ave)

t = np.arange(len(c))
twap = np.average(c,weights=t)#时间加权
print(twap)

print(np.max(c))#最大值
print(np.min(c))#最小值
print(np.ptp(c))#区间 最大值-最小值

print(np.median(c))#中位数
print(np.msort(c))

print(np.var(c))#方差

returns = np.diff(np.log(c))#对数收益率
print(returns)
print(np.where(returns>0))
print('')

import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
print('--------------------')
weights = [0, 1, 0.5]
c = [1, 2, 3]
sma = np.convolve([1, 2, 3], [0.5,0.5, 0.5])#卷积，补充卷积概念
print(sma)
t = np.arange(3)
plot(t,c[:],lw=1.0)
t = np.arange(len(sma))
plot(t,sma,lw=2.0)
show()