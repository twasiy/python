import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


# x_1 = np .linspace(0,5,10)
# y_1 = x_1**2

# fig_1 = plt.figure(figsize=(5,4),dpi=100)
# axes_1 = fig_1.add_axes([0.1,0.1,0.85,0.85])
# axes_1. set_xlabel('days')
# axes_1. set_ylabel('days squred')
# axes_1. set_title('days squred chart')
# axes_1.plot(x_1,y_1,label = 'x/x**2')
# axes_1.plot(y_1,x_1,label = 'x**2/x')
# axes_1.legend(loc = 0)

# axes_2 = fig_1.add_axes([0.37,0.37,0.4,0.4])
# axes_2. set_xlabel('days')
# axes_2. set_ylabel('days squred')
# axes_2. set_title('days squred chart')
# axes_2.plot(x_1,y_1)
# axes_2.plot(y_1,x_1)
# axes_2.text(0,33,'Massege')


# x_data = np .random.random(1000) *100
# y_data = np .random.random(1000) *100
# plt.scatter(x_data,y_data,c = '#00f',s = 150,marker='*',alpha=0.35)


# plt.show()

x = ['c++','c#','java','python','javascript','Go','Assembly']
y = [80,21,56,86,64,13,9]

plt.pie(y,labels=x)

plt.grid(True)
plt.show()