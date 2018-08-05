import numpy as np  
import matplotlib
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.style.use("ggplot")

# 分成2x2，占用第一个，即第一行第一列的子图

data =  pd.read_excel("C:\\Users\\admin\\Desktop\\副本万科京东数据(1).xlsx",sheetname='数据采集表')
# print(list(data['冷机耗电量']))
x=data["时间"]
sh = data["冷机耗电量"]
zh = data["室内温度1"]
# nx = data[["冷机耗电量","时间戳","室内温度1"]].groupby('冷机耗电量')
# print(nx)
nx = data[(sh == "停机" )]
ne = data[(sh != "停机")]

print(ne[['时间2','室内温度1']])
print(nx[['时间2','室内温度1']])


plt.figure(1)
plt.xlabel(u"日期-时间戳") #X轴标签
plt.ylabel("冷冻水供回水温差————耗电量的log2对数————室内平均温度————室外温度") #Y轴标签
# plt.title("") #标题
plt.subplot(331)
plt.xlabel(u"室内温度1") #X轴标签
plt.scatter(ne['时间戳'],ne['室内温度1'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度1'],color='gray',s=17,label='机组停机')
plt.subplot(332)
plt.xlabel(u"室内温度2") #X轴标签
plt.scatter(ne['时间戳'],ne['室内温度2'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度2'],color='gray',s=17,label='机组停机')

plt.subplot(333)
plt.scatter(ne['时间戳'],ne['室内温度3'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度3'],color='gray',s=17,label='机组停机')
plt.xlabel(u"室内温度3") #X轴标签
plt.subplot(334)
plt.scatter(ne['时间戳'],ne['室内温度4'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度4'],color='gray',s=17,label='机组停机')
plt.xlabel(u"室内温度4") #X轴标签
plt.subplot(335)
plt.xlabel(u"室内温度5") #X轴标签
plt.scatter(ne['时间戳'],ne['室内温度5'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度5'],color='gray',s=17,label='机组停机')
plt.subplot(336)
plt.xlabel(u"室内温度6") #X轴标签
plt.scatter(ne['时间戳'],ne['室内温度6'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度6'],color='gray',s=17,label='机组停机')


plt.subplot(337)
plt.xlabel(u"室内温度7") #X轴标签
plt.scatter(ne['时间戳'],ne['室内温度7'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度7'],color='gray',s=17,label='机组停机')
plt.subplot(338)
plt.scatter(ne['时间戳'],ne['室内温度8'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度8'],color='gray',s=17)
plt.xlabel(u"室内温度8") #X轴标签

plt.subplot(339)
plt.scatter(ne['时间戳'],ne['室内温度10'],color='g',s=12,label='机组停机')
plt.xticks([])
plt.scatter(nx['时间戳'],nx['室内温度10'],color='gray',s=17)
plt.xlabel(u"室内温度9") #X轴标签

plt.margins(0)
plt.subplots_adjust(bottom=0.15)

plt.show()
