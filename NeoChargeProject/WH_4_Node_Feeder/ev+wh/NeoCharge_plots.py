import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from datetime import timedelta
df1 = pd.read_csv('house_meter.csv',usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
df2 = pd.read_csv('house_meter.csv',usecols=['measured_real_power'],engine='python')
x1 = df2['measured_real_power']
#y1 = [dt.datetime.now() + dt.timedelta(milliseconds=i) for i in range(len(x1))]
y1 = df1['# timestamp']
plt.plot(y1,x1)
#plt.gcf().autofmt_xdate()
plt.xticks(rotation=90)
plt.show()

print(x1)
