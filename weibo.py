import xlrd
from matplotlib.pyplot import *
from matplotlib.pyplot import *


file = 'news.xls'

wb = xlrd.open_workbook(file)       #导入文件
ws = wb.sheet_by_name('Sheet1')     #导入Sheet1
sheet1 = wb.sheet_by_index(0)       #通过目录导入


cols = sheet1.col_values(9)         #导入第10列的数据
temp = ' '.join(cols)               #将第十列数据存为str类型
data_weiboLevel_x = temp.split( )   #去除空格
del data_weiboLevel_x[0]            #删除第一个元素
count = 0   

for i in data_weiboLevel_x[:]:      # 计算并移除"不显示"的字符串
    if i == "不显示":
        count += 1
        data_weiboLevel_x.remove(i)
    else:
        data_weiboLevel_x += i


data_weiboLevel_y = []              #y轴数据
data_x = []                         #x轴数据
new_data_weiboLevel_x = []          #int数据的列表


for r in data_weiboLevel_x:
    new_data_weiboLevel_x.append(int(r))
new_data_weiboLevel_x.sort()
new_data_weiboLevel_x.append(" ")       

def num_data(list1, list2, list3):              #list1:int型列表总数据 
    a = 0                                       #list2:y轴数据
    t = -1                                      #list3:x轴数据
    try:
        for num in list1:
            if list1[a] == list1[a+1]:
                pass
            else:
                list3.append(list1[a])
                list2.append(a - t)
                t = a
            a += 1
        list3.append(48)
    except:
        pass

num_data(new_data_weiboLevel_x, data_weiboLevel_y, data_x)

data_x.append("不显示")
data_weiboLevel_y.append(count)
#print(new_data_weiboLevel_x, data_weiboLevel_y, data_x)


x = data_x

y = data_weiboLevel_y

 

#create new figure

figure("虚假新闻")

 

#线


plot(x,y)

 


show()