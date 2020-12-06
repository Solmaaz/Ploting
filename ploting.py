import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os 
import math

path = '/home/solmaz/ploting/data1'
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
    plt.figure(figsize=(12,12))
    plt.subplot(2,2,1)
    plt.plot(time,phase)
    plt.title('phase difference')
    plt.subplot(2,2,2,polar='True')
    #ax4 = plt.subplot(polar='True')# plt.hist(theta0, bins=np.arange(min(theta0),max(theta0),.1), bottom=10, color="black") n, bins, patches = plt.hist(theta_befor_stim,bins=np.arange(min(theta_after_stim),max(theta_after_stim),0.025),alpha=0.7,color="blue",bottom=10)
    n, bins, patches = plt.hist(sf,alpha=0.7,color="blue",bottom=50) 
    plt.xticks([]) 
    plt.title('phase dif histogram')
    plt.subplot(2,2,3)
    sns.distplot(cosine)
    plt.title('PDF cos(phase diff)')
    plt.subplot(2,2,4)
    grid = sns.distplot(cosine)
    grid.set(yscale= "log")
    plt.title('log PDF cos(phase diff)')
    plt.savefig(str(name)+'.png')
    #plt.savefig('m'+str(name)+'.eps', format = eps)
    #number.loc[name]=(name[0:-4])

#sns.distplot(df)
#plt.show()


#plt.yticks([]) 
#filename='theta_tp={:08.4}'.format(it_stim*dt) extension="_.png" 
#filename=filename+extension plt.savefig(filename,dpi=300)
#plt.show()
#bins=np.arange(min(df),max(df),0.1),