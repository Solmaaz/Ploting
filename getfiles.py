import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os 
import math
import scipy.optimize as opt
path = '/home/solmaz/ploting/data1'
names= os.listdir(path)
print(names)
number = pd.DataFrame(columns=['xdata','ydata', 'Y', 'F','X'], index=names)
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
    #plt.subplot(1,2,1)
    xdata, ydata = sns.distplot(cosine).get_lines()[0].get_data()
    Y = np.log(ydata)
    #print(ydata)
    #print(Y)
    F = func(xdata)
    X = F + Y
    #number.loc[name].num = name[0:-4]
    number['xdata'] = [xdata]
    number['ydata'] = [ydata]
    number['Y'] = [Y]
    number['F'] = [F]
    number['X'] = [X]
    plt.show()
    print(number)
    number.to_csv(r'/home/solmaz/ploting/fitting.txt', header=None, index=None, sep=' ', mode='a')