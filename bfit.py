import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os 
import math
import scipy.optimize as opt
path = '/home/solmaz/ploting/data'
names= os.listdir(path)
print(names)

def func(x):
    P = np.power(x,2)
    return ((0.5) *np.log(1-P))
for name in names:
    add = os.path.join(path,name)
    data=np.loadtxt(add)
    time = data[:,0]
    phase = data[:,4]
    num = name[0:-4]
    sf = phase*np.pi
    cosine = np.cos(sf)
    plt.figure(1)
    xdata, ydata = sns.distplot(cosine).get_lines()[0].get_data()
    Y = np.log(ydata)
    plt.legend()
    #print(ydata)
    #print(Y)
    F = func(xdata)
    X = F + Y
    plt.figure(2)
    bp = plt.plot(xdata, X, label='b')
    plt.legend()
    print(bp)
plt.savefig('b.png')
plt.show()

    
    #print(X)
    #plt.subplot(1,2,2)
    #plt.plot(xdata, X, label="b")
    #plt.title('')
    #plt.legend()
    #plt.savefig(str(name)+'.png')
    #plt.show()