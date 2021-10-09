
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from datetime import datetime
df1 = pd.read_csv('house_meter.csv',usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
df2 = pd.read_csv('house_meter.csv',usecols=['measured_real_power'])
df3 = pd.read_csv('house_meter_cont.csv',usecols=['# timestamp'],parse_dates=['# timestamp'],engine='python')
df4 = pd.read_csv('house_meter_cont.csv',usecols=['measured_real_power'])
print(df3,df4)

def plots(x_axis,y_axis,x1_axis,y1_axis):
    
    x = df1['# timestamp']
    y = df2['measured_real_power']
    x1 = df3['# timestamp']
    y1 = df4['measured_real_power']
    fig, (ax1,ax2) = plt.subplots(2,1,sharex=True)
    ax1.plot(x,y)
    ax2.plot(x1,y1)

    ax1.grid()
    ax2.grid()
    plt.xticks(rotation=25)
    ax1.title.set_text('EV+WH w/o Switch')
    ax2.title.set_text('EV+WH w Switch')
    ax1.set(ylabel='Power in Watts')
    ax2.set(ylabel='Power in Watts')
#    plt.xlabel('Time')
#    plt.ylabel('Power in Watts')
    ax1=plt.gca()
    xfmt = md.DateFormatter('%H:%M:%S')
    ax1.xaxis.set_major_formatter(xfmt)
    plt.show()
plots(df1,df2,df3,df4)

#df5 = pd.read_csv('house_meter_cont.csv',usecols=['# timestamp','measured_real_power'],parse_dates=['# timestamp'])
#df5.plot(x="# timestamp", y="measured_real_power")
#plt.grid()
#plt.xlabel("Time")
#plt.ylabel("Power in watts")
#plt.show()

