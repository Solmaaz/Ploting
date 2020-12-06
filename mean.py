import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt('number.txt')
m = data[:,0]
mean = data[:,1]
std = data[:,2]
plt.figure(figsize=(12,3))
plt.subplot(1,2,1)
plt.scatter(m,mean)
plt.xlabel('m')
plt.ylabel('Phase dif. mean')
plt.subplot(1,2,2)
plt.scatter(m,std)
plt.xlabel('m')
plt.ylabel('Phase dif. std')
plt.savefig('mean-std.png')
plt.show()