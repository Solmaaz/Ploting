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
    #cosine = np.cos(data)
    sf = phase*np.pi
    cosine = np.cos(sf)
    #plt.figure(figsize=(6,6))
    #plt.subplot(1,2,1)
    #grid = sns.distplot(cosine, label=" log PDF") 
    #grid.set(yscale= "log")
    #plt.figure(0)
    xdata, ydata = sns.distplot(cosine).get_lines()[0].get_data()
    Y = np.log(ydata)
    #print(ydata)
    #print(Y)
    F = func(xdata)
    X = F + Y
    plt.plot(xdata,ydata, label="PDF")
    plt.plot(xdata, Y, label= "log PDF")
    plt.plot(xdata, F, label= "F")
    #plt.figure(1)
    plt.plot(xdata, X, label="b")
    plt.legend()
    plt.savefig(str(name)+'.png')
    plt.show()

    
    #print(X)
    #plt.subplot(1,2,2)
    #plt.plot(xdata, X, label="b")
    #plt.title('')
    #plt.legend()
    #plt.savefig(str(name)+'.png')
    #plt.show()