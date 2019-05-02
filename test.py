
from matplotlib.pyplot import *
from weibo import data_x,data_weiboLevel_y,count
 

x = data_x

y = data_weiboLevel_y

 

#create new figure

figure("虚假新闻")

 

#线


plot(x,y)

 


show()