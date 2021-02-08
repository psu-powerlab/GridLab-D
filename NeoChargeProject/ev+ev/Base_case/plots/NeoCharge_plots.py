import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime
'''
df1 = pd.read_csv('house_meter_cont.csv',usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
df2 = pd.read_csv('house_meter_cont.csv',usecols=['measured_real_power'])

def plots(x_axis,y_axis):
    
    x = x_axis['# timestamp']
    y = y_axis['measured_real_power']
    plt.plot(x,y)
    plt.grid()
    plt.xticks(rotation=25)
    plt.gca()
    plt.show()
plots(df1,df2)
'''

file1 = 'ev1_base_case.csv'
timestamp = pd.read_csv(file1,usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
power = pd.read_csv(file1,usecols=['measured_real_power'],engine='python')

file2 = 'ev2_base_case.csv'
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
plt.legend(loc = 'upper left')
plt.title('With NeoCharge')
plt.xlabel('Time')
plt.ylabel('Power (Watts)')
plt.grid()
plt.xticks(rotation=25)
plt.gca()
plt.show()

# df1 = pd.read_csv('house_meter_cont.csv',usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
# df2 = pd.read_csv('house_meter_cont.csv',usecols=['measured_real_power'])

# x = df1['# timestamp']
# y = df2['measured_real_power']
# plt.plot(x,y)
# plt.grid()
# plt.xticks(rotation=25)
# plt.gca()
# plt.show()



# def subplots(x_axis,y_axis,x1_axis,y1_axis):
    
#     x = df1['# timestamp']
#     y = df2['measured_real_power']
#     x2 = df3['# timestamp']
#     y2 = df4['measured_real_power']
#     plt.plot(x,y,label='Primary_EV1')
#     plt.plot(x2,y2,label='Secondary_EV2')
#     plt.title('Without NeoCharge')
#     plt.grid()
#     plt.legend()
#     plt.gcf().autofmt_xdate()
#     plt.show()
# plots(df1,df2,df3,df4)
