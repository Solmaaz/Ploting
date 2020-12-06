import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os 
import math

path = '/home/solmaz/ploting/data'
names= os.listdir(path)
print(names)
#names = names[:3]
#print(names)
#df_main =pd.DataFrame()
for name in names:
    add = os.path.join(path,name)
    data=np.loadtxt(add)
    time = data[:,0]
    phase = data[:,4]
    #cosine = np.cos(data)
    sf = phase*np.pi
    cosine = np.cos(sf)  
    
    plt.figure(figsize=(12,18))
    plt.subplot(2,2,1)
    plt.plot(time,phase)
    plt.title('phase difference')
    plt.subplot(2,2,2,polar='True')
    #ax4 = plt.subplot(polar='True')# plt.hist(theta0, bins=np.arange(min(theta0),max(theta0),.1), bottom=10, color="black") n, bins, patches = plt.hist(theta_befor_stim,bins=np.arange(min(theta_after_stim),max(theta_after_stim),0.025),alpha=0.7,color="blue",bottom=10)
    n, bins, patches = plt.hist(sf,alpha=0.7,color="blue",bottom=50) 
    plt.xticks([]) 
    plt.title('phase dif histogram')