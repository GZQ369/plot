import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.style.use("ggplot")
#matplotlib.style.use("dark_background")

ls = pd.read_excel('万科京东数据采集表7.6.xlsx2.xlsx',sheetname="数据采集表")

labels=['室外温度','室内平均温度','整体耗电量','冷冻水供回水温差']
'''sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0'''
names = ['2018/7/5', '2018/7/6', '2018/7/6', '2018/7/7', '2018/7/8','2018/7/9','2018/7/10','2018/7/11','2018/7/12','2018/7/13','2018/7/14','2018/7/15','2018/7/16','2018/7/17','2018/7/18']
x = ls["时间"]
y1=ls['室内温度1']
y2=ls['室内温度2']
y3=ls['室内温度3']
y4=ls['室内温度4']
y5=ls['室内温度5']
y6=ls['室内温度6']
y7=ls['室内温度7']
y8=ls['室内温度8']
y9=ls['室内温度9']
y10=ls['室内温度10']

plt.figure(1)
#plt.plot(x,y,linewidth=1,marker='^', color='blue',mec='darkblue', ms=4 ,mfc='w',label=u'室外温度')
plt.plot(x,y1,label=u'室内温度1')
plt.plot(x,y2,label=u'室内温度2')
plt.plot(x,y3,label=u'室内温度3')
plt.plot(x,y4,label=u'室内温度4')
plt.plot(x,y5,label=u'室内温度5')
plt.plot(x,y6,label=u'室内温度6')
plt.plot(x,y7,label=u'室内温度7')
plt.plot(x,y8,label=u'室内温度8')
plt.plot(x,y9,label=u'室内温度9')
plt.plot(x,y10,label=u'室内温度10')
plt.legend()  # 让图例生效

plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"时间") #X轴标签
plt.ylabel("室内温度") #Y轴标签
plt.title("不同室内温度——时间分布图") #标题

#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.show()
# plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.show()
exit()
z1 = np.polyfit(xe['冷冻水供回水温差'],xe['冷机耗电量'], 3)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(xe['冷冻水供回水温差'])#也可以使用yvals=np.polyval(z1,x)
# # plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(xe['冷冻水供回水温差'], yvals, 'r',label=u'相关系数为：0.0262261166464')
plt.plot(s, -7.332 *s**3 + 73.68 *s**2 - 144.4 *s + 56.14,'g')#,label=u'相关系数为：0.0262261166464')
# #plt.plot(x,m,linewidth=1,color='red')#平均室温
# plt.plot(le,n,linewidth=2, color='g',label=u'相关系数为：0.337179389096')#耗电量
#plt.scatter(x,le,linewidth=1,marker='v', color='y',ms=4,  mfc='w',label=u'冷冻水供回水温差')
#mfc='w'表示空心     mec='g'表示标记的颜色绿色  ms=3表示空心的范围大小
