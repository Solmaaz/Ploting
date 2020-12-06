import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os 
import math
import scipy.optimize as opt
from scipy.integrate import quad
import scipy.special as sp



path = '/home/solmaz/ploting/data1'
names= os.listdir(path)
print(names)
#names = names[:3]
#print(names)
#df_main =pd.DataFrame()
def func(x, b):
    P = np.power(x,2)
    return ((np.exp(b * x))/(np.sqrt(1-P)))
for name in names:
    add = os.path.join(path,name)
    data=np.loadtxt(add)
    time = data[:,0]
    phase = data[:,4]
    #cosine = np.cos(data)
    sf = phase*np.pi
    cosine = np.cos(sf)
    #grid = sns.distplot(cosine)
    xdata, ydata = sns.distplot(cosine).get_lines()[0].get_data()
    #print(xdata)
    #print(ydata)
    #plt.plot(xdata,ydata)
    #plt.show()
    #popt, pcov = so.curve_fit(func, xdata, ydata)
    #plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    #plt.show()
    #myPlot = sns.distplot(cosine)
    #logy = np.log(ydata)
    # Fine Line2D objects
    #lines2D = [obj for obj in myPlot.findobj() if str(type(obj)) == "<class 'matplotlib.lines.Line2D'>"]
    
    # Retrieving x, y data
    #x, y = lines2D[idx].get_data()[0], lines2D[idx].get_data()[1]
    
    # Store as dataframe 
    #data.append(pd.DataFrame({'x':x, 'y':y}))
    #plt.plot(data[0].x, data[0].y)
    grid = plt.plot(xdata, ydata, ".", label="Data")
    #grid.set(yscale= "log")
    # The actual curve fitting happens here
    optimizedParameters, pcov = opt.curve_fit(func, xdata, ydata, maxfev=5000)
    #Y = func(xdata, optimizedParameters)
    #ans, err = quad( Y , -0.99999, 0.99999)
    #print(ans)
    print(*optimizedParameters)
    Y = func(xdata, *optimizedParameters)/(math.pi*sp.jv(0,1))
    # Use the optimized parameters to plot the best fit
    drd=plt.plot(xdata,Y , label="fit")
    #drd.set(yscale= "log")
    # Show the graph
    plt.legend()
    plt.title('fiting to PDF cos(phase diff)')
    plt.savefig(str(name)+'.png')
    plt.show()