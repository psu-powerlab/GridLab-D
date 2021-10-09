import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import datetime as dt
from datetime import timedelta
import time




df = pd.read_csv("wh_E_1.csv")
df1 = pd.read_csv("wh_hp_1.csv")



x1 = df['# timestamp']

y1 = df['water_demand']

y11 = df['is_waterheater_on']

y2 = df1['water_demand']

y22 = df1['is_waterheater_on']

#x1 = [dt.datetime.now() + dt.timedelta(minutes=i) for i in range(len(y1))]
fig,ax = plt.subplots(2,figsize=(10,15),sharey=True)
ax[0].plot(x1,y1)
ax[0].set_ylabel('EWH state')
ax[0].plot(x1,y11)
ax[0].set_title('EWH')
ax[0].set_ylabel('water_demand')
ax0 = ax[0].twinx()
plt.legend()

ax[1].plot(x1,y2,label="HPWH_water_demand")
ax[1].plot(x1,y22,label="HPWH_state")
ax[1].set_title('HPWH')
ax1=ax[1].twinx()

plt.show()


