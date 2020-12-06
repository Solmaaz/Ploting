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
    phase = data[:,2]
    cosine = np.cos(data)
    sf = phase*np.pi
    y = math.modf(sf)
print(sf)
print(y[:,1])