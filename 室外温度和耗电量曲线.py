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

labels=['室外温度','室内平均温度','整体耗电量','冷冻水供回水温差']
'''sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0'''
names = ['2018/7/5', '2018/7/6', '2018/7/6', '2018/7/7', '2018/7/8','2018/7/9','2018/7/10','2018/7/11','2018/7/12','2018/7/13','2018/7/14','2018/7/15','2018/7/16','2018/7/17','2018/7/18']
x = ls["时间"]
y = ls["气温"]
z = ls["耗电量"]#取耗电量以lg10为底的对数
le = ls["冷冻水回水温度"]-ls["冷冻水供水温度"]
m = ls["平均室温"]
n = ls["冷机耗电量"]
sh = ls["升温"]
plt.figure(1)
#plt.plot(x,y,linewidth=1,marker='^', color='blue',mec='darkblue', ms=4 ,mfc='w',label=u'室外温度')
print(y.corr(n))
# nx = ls[["冷机耗电量","气温"]].groupby('气温').mean()
# print(nx["冷机耗电量"])
# a,b,c = ls[["冷机耗电量","气温","升温"]].groupby('升温')
nx = ls[(sh>0)]
print(nx[["气温","冷机耗电量"]])
ze = ls[(sh==0)]
jx = ls[(sh<0)]
plt.scatter(nx["气温"],nx["冷机耗电量"],color='r',s=17,label='温度上升')
plt.scatter(ze["气温"],ze["冷机耗电量"],color='g',s=17,label='温度不变')
plt.scatter(jx["气温"],jx["冷机耗电量"],color='b',s=17,label='温度下降')
# xf = ls[["气温","冷机耗电量"]]
# xe = xf.drop_duplicates('气温') #删除重复气温的行
# # print(xe)
# z1 = np.polyfit(xe['气温'], xe['冷机耗电量'], 3)#用3次多项式拟合
# p1 = np.poly1d(z1)
# print(p1) #在屏幕上打印拟合多项式
# yvals=p1(xe['气温'])#也可以使用yvals=np.polyval(z1,x)
# # plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(xe['气温'], yvals, 'r',label=u'相关系数为：0.337179389096')

#plt.plot(x,m,linewidth=1,color='red')#平均室温
# plt.plot(nx['冷机耗电量'],linewidth=2, color='g',label='')#耗电量
# plt.ylim(125,400)
# plt.scatter(y,n,color='g',s=17)
#mfc='w'表示空心     mec='g'表示标记的颜色绿色  ms=3表示空心的范围大小
plt.legend()  # 让图例生效

plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"室外温度") #X轴标签
plt.ylabel("耗电量") #Y轴标签
plt.title("室外温度——耗电量关系图") #标题

#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.show()
