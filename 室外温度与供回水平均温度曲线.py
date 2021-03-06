import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
matplotlib.style.use("ggplot")
#matplotlib.style.use("dark_background")

ls = pd.read_excel('万科京东数据采集表7.6.xlsx2.xlsx',sheetname="数据采集表")

x = ls["时间"]
y = ls["气温"]
df = ls["平均温度"]
z = ls["耗电量"]#取耗电量以lg10为底的对数
le = ls["冷冻水回水温度"]-ls["冷冻水供水温度"]
m = ls["平均室温"]
n = ls["冷机耗电量"]
sh = ls["升温"]
s = np.arange(21,36 , 1)
plt.figure(1)
# nx = ls[["耗电量","气温","平均温度"]].groupby('气温').mean()
# print(nx["耗电量"])

nx = ls[(sh>0)]
print(nx[["气温","平均温度"]])
ze = ls[(sh==0)]
jx = ls[(sh<0)]
plt.scatter(nx["气温"],nx["平均温度"],color='r',s=17,label='温度上升')
plt.scatter(ze["气温"],ze["平均温度"],color='g',s=17,label='温度不变')
plt.scatter(jx["气温"],jx["平均温度"],color='b',s=17,label='温度下降')
#plt.plot(x,y,linewidth=1,marker='^', color='blue',mec='darkblue', ms=4 ,mfc='w',label=u'室外温度')
print(y.corr(df))
# xf = ls[["气温","平均温度"]]
# xe = xf.drop_duplicates('气温') #删除重复气温的行
# print(xe)
# z1 = np.polyfit(xe['气温'], xe['平均温度'], 3)#用3次多项式拟合
# p1 = np.poly1d(z1)
# print(p1) #在屏幕上打印拟合多项式
# yvals=p1(xe['气温'])#也可以使用yvals=np.polyval(z1,x)
# plot1=plt.plot(x, y, '*',label='original values')
# plt.plot(xe['气温'], yvals, 'r',label=u'相关系数为：-0.258763650505')

# plt.plot(s, -0.01241*s**3 + 1.054 *s**2 - 29.68 *s + 287.2,'g')


#plt.plot(x,m,linewidth=1,color='red')#平均室温
# plt.plot(nx['平均温度'],linewidth=2, color='g')#耗电量
# plt.ylim(7.0, 15.0)
# plt.scatter(y,df,s=18,label=u'冷冻水供回水温度')
#mfc='w'表示空心     mec='g'表示标记的颜色绿色  ms=3表示空心的范围大小
plt.legend()  # 让图例生效

plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"室外温度") #X轴标签
plt.ylabel("供回水平均温度") #Y轴标签
plt.title("室外温度——供回水平均温度") #标题

#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.show()
