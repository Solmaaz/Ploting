import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = '/home/solmaz/ploting/data0'
names= os.listdir(path)
print(names)
number = pd.DataFrame(columns=['num','Mean','Std'], index=names)
for name in names:
    print(name)
    add = os.path.join(path,name)
    data=np.loadtxt(add)
    #data=np.loadtxt(name)
    time = data[:,0]
    phase = data[:,6]
    #pd=float(name)
    #print(pd)
    number.loc[name].num = name[0:-4]
    number.loc[name].Mean = phase.mean()
    number.loc[name].Std =phase.std()
print(number)
number.to_csv(r'/home/solmaz/ploting/number.txt', header=None, index=None, sep=' ', mode='a')
#plt.plot(time,phase)
#plt.title('phase difference')