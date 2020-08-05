import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,30,80,90,80,78,67,54,23]

x1=[1,2,3,4,5,6,7,8,9,10]
y1=[11,23,45,65,76,78,98,45,67,20]

plt.xlabel('days')
plt.ylabel('amt')
plt.title('trans_box\nA and B')

plt.plot(x,y,label='A')
plt.plot(x1,y1,label='B')
plt.legend()
plt.show()
