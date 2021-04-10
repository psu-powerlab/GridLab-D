import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime

file1 = 'house_meter_cont.csv'
timestamp = pd.read_csv(file1,usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
power = pd.read_csv(file1,usecols=['measured_real_power'],engine='python')

file2 = 'house_meter_noNC.csv'
power2 = pd.read_csv(file2,usecols=['measured_real_power'],engine='python')

x = timestamp['# timestamp']
y = power['measured_real_power']
x1 = timestamp['# timestamp']
y1 = power2['measured_real_power']
fig, (ax1,ax2) = plt.subplots(2,1,sharex=True)
a,b = 0,4000
ax1.plot(x1,y1)
ax2.plot(x,y)
ax1.grid()
ax2.grid()
plt.xticks(rotation=25)
ax1.title.set_text('EV+EV w/o Switch')
ax2.title.set_text('EV+EV w Switch')
ax1.set(ylabel='Power in Watts')
ax2.set(ylabel='Power in Watts')
ax2.set(xlabel='Time')
ax1.set_ylim(a,b)
ax2.set_ylim(a,b)
#    plt.xlabel('Time')
#    plt.ylabel('Power in Watts')
ax1=plt.gca()
xfmt = md.DateFormatter('%H:%M:%S')
ax1.xaxis.set_major_formatter(xfmt)
plt.show()
