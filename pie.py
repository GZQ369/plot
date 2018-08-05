import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
plt.style.use("ggplot")

sizes = [16, 35, 20, 29]
colors = ['red',  'blue', 'green','white']
explode = (0.05, 0.05, 0.05,0)
# 农业每次贡献总收益的16%，其中农、林、牧、渔业各贡献4%；
# 工业每次贡献总收益的35%，其中采矿业贡献15%，制造业贡献10%，建筑业贡献10%；
# 服务业每次贡献总收益的20%，其中科教文卫体贡献5%，餐饮业贡献5%，娱乐业贡献7%，金融业贡献3%。
import matplotlib.pyplot as plt             # [4,15,5]  [4,10,5]  [4,10,7] [4,0,3]
import matplotlib
ind = np.arange(3)
a = np.array([4,0,0])
a2 = np.array([0,15,0])
a3 = np.array([0,0,5])

b = np.array([4, 0, 0])
b2 = np.array([0, 10, 0])
b3 = np.array([0,0,5])

c = np.array([4,0,0])
c2 = np.array([0,10,0])
c3 = np.array([0,0,7])

d = np.array([4,0,0])
d2 = np.array([0,0,0])
d3 = np.array([0,0,3])

p1 = plt.bar(ind, a, 0.45,color='red',alpha=0.8,label='农业')
p2 = plt.bar(ind, a2, 0.45,color ='brown', alpha=0.8,bottom=sum([a]),label='采矿业') 
p3 = plt.bar(ind, a3, 0.45,color= 'c' , alpha=0.8, bottom=sum([a, a2]),label='科教文卫体')
p4 = plt.bar(ind, b, 0.45, color='black', alpha=0.8, bottom=sum([a, a2, a3]),label='林业')
p5 = plt.bar(ind, b2, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b]),label='制造业')
p6 = plt.bar(ind, b3, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2]),label='餐饮业')
p7 = plt.bar(ind, c, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3]),label='牧业')
p8 = plt.bar(ind, c2, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3,c]),label='建筑业')
p9 = plt.bar(ind, c3, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3,c,c2]),label='娱乐业')
p9 = plt.bar(ind, d, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3,c,c2,c3]),label='渔业')
p10 = plt.bar(ind, d2, 0.45,  alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3,c,c2,c3,d]),label='')
p11 = plt.bar(ind, d3, 0.45, color='yellow', alpha=0.8, bottom=sum([a, a2, a3,b,b2,b3,c,c2,c3,d]),label='金融业')





label_list = [u'农业', u'工业', u'服务业']
# list1 = np.array([4,15,5])
# list2 = np.array([4, 10, 5])
# list3 = np.array([4,10,7])
# list4 = np.array([4,0, 3])
x = range(3)

# print(x)

# rects1 = plt.bar(left=x, height=list1, width=0.45, alpha=0.8, color='red', label="")
# rects2 = plt.bar(left=x, height=list2, width=0.45, color='green', label="",bottom=sum([list1]))
# rects3 = plt.bar(left=x, height=list3, width=0.45, alpha=0.8, color='blue', label="",bottom=sum(list1+list2))
# rects4 = plt.bar(left=x, height=list4, width=0.45, alpha=0.8, color='yellow', label="",bottom=sum(list3+num_list2))

plt.ylabel("百分比（%）")
plt.xticks(x, label_list)
plt.xlabel("")
plt.title("")
plt.legend()
plt.show()