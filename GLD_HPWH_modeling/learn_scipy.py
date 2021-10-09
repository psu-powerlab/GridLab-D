import pandas as pd
import numpy as np
from scipy.integrate import quad
from scipy.integrate import trapz as tz

sample_x = np.linspace(0,np.pi,1000)
sample_y = np.sin(sample_x)
result = tz(sample_y,sample_x)
print('sample_x ------------>\n',type(sample_x))
#print('sample_y ---------->\n',sample_y)
#print('results ------------>\n',result)
watts = []
minutes = []
for i in df.iloc[:,10]: #consumed watts col
    watts.append(i)
for k in df.iloc[:,13]: # Heating index.
    minutes.append(k)
