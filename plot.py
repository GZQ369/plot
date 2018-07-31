import matplotlib.pyplot as plt
import math
import pandas as pd
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.style.use("ggplot")
#matplotlib.style.use("dark_background")

ls = pd.read_excel('万科京东数据采集表7.6.xlsx2.xlsx',sheetname="数据采集表")

labels=['室外温度','室内平均温度','整体耗电量','冷冻水供回水温差']
'''sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
'''
names = ['2018/7/5', '2018/7/6', '2018/7/6', '2018/7/7', '2018/7/8','2018/7/9','2018/7/10','2018/7/11','2018/7/12','2018/7/13','2018/7/14','2018/7/15','2018/7/16','2018/7/17','2018/7/18']
x = ls[["时间"]]
y = ls[["气温"]]
z = ls["耗电量"]#取耗电量以lg10为底的对数
le = ls["冷冻水回水温度"]-ls["冷冻水供水温度"]
m = ls["平均室温"]
plt.figure(1)

# z1 = np.polyfit(x, y, 3)#用3次多项式拟合
# p1 = np.poly1d(z1)  #拟合出多项式方程
# #print(p1) #在屏幕上打印拟合多项式
# yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
# plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(x, yvals, 'r',label='polyfit values')

plt.plot(x,y,linewidth=1,marker='^', color='blue',mec='darkblue', ms=4 ,mfc='w',label=u'室外温度')


plt.plot(x,m,linewidth=1,color='red')#平均室温
plt.plot(x,z,linewidth=1,marker='o', mec='darkgreen', color='g', ms=4, mfc='w',label='耗电量的log2对数')#耗电量
plt.plot(x,le,linewidth=1,marker='v', color='y',ms=4,  mfc='w',label=u'冷冻水供回水温差')
#mfc='w'表示空心     mec='g'表示标记的颜色绿色  ms=3表示空心的范围大小
plt.legend()  # 让图例生效

plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"日期-时间") #X轴标签
plt.ylabel("冷冻水供回水温差————耗电量的log2对数————室内平均温度————室外温度") #Y轴标签
plt.title("") #标题

#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.show()
plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号