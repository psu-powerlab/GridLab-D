
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime

file1 = 'ev1.csv'
timestamp = pd.read_csv(file1,usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
power = pd.read_csv(file1,usecols=['measured_real_power'],engine='python')

file2 = 'ev2.csv'
power2 = pd.read_csv(file2,usecols=['measured_real_power'],engine='python')

# x1 = timestamp['# timestamp']
# x1 = timestamp.iloc[1300:2763,0]
# y1 = power['measured_real_power']
# y1 = power.iloc[1300:2763,0]
# y2 = power2['measured_real_power']
# y2 = power2.iloc[1300:2763,0]
# plt.figure(figsize=(15,7))
# plt.plot(x1,y1,label='Primary_EV')
# plt.plot(x1,y2,label='Secondary_EV')
# plt.legend(loc = 'upper left')
# plt.title('W/O NeoCharge')
# plt.xlabel('Time')
# plt.ylabel('Power (Watts)')
# plt.grid()
# plt.xticks(rotation=25)
# plt.gca()
# plt.show()



file3 = 'house_meter_cont.csv'
timestamp = pd.read_csv(file3,usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
power = pd.read_csv(file3,usecols=['measured_real_power'],engine='python')

x1 = timestamp['# timestamp']
x1 = timestamp.iloc[1300:2800,0]
y1 = power['measured_real_power']
y1 = power.iloc[1300:2800,0]
plt.figure(figsize=(15,7))
plt.plot(x1,y1)
#plt.legend(loc = 'upper left')
plt.title('EV_EV With NeoCharge')
plt.xlabel('Time')
plt.ylabel('Power (Watts)')
plt.grid()
plt.xticks(rotation=25)
plt.gca()
plt.show()
