# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 00:19:34 2020

@author: 雷霆
"""


import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('D:/Git/work_code/example_csv.txt',delimiter=',',
            unpack=True)

plt.plot(x,y,label='load data from csv file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('asdasdas\nnijjiji')
plt.legend()
plt.show()