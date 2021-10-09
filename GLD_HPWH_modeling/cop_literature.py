import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import math
from curlyBrace import curlyBrace
'''
The following cop equation was taken from the following sources:
    
    - Heat pump water heater technology assessment based on laboratory research and energy ssimulation models

    - Field performance of the heat pump water heaters in the northwest.

Both docs can be found MacBook's desktop, publications folder.

path ~/Desktop/Parallels\ Shared\ Folders/Desktop/Publications

'''
# I'll be using one of the EMCB testing files. Keep in mind any EMCB testing file should be when EMCBs are closed and no loadup command is applied. 

path ='/home/parallels/Desktop/thesis_work/csv_files/hpwh_no_load_up_emcb_closed.csv'

df = pd.read_csv(path)


###### Clean data ######

def clean_data():
    df = df.drop(['idk','idk2','rated_real_power','idk3','max_watts_hour','idk4','idk5','idk6','idk7'],axis=1)
    return df


####### Convert EnergyTake values to Temperature:####### 

def ET_Temp(df):
    
    E_take = df['real_available_Wh']

    df['tank_temp'] = (120 - (df['real_available_Wh']/122))

    df['time'] = pd.to_datetime(df['timestamp']).dt.strftime('%H:%M') # Change time format for simplicity

    df = df.drop(['timestamp'],axis=1)

    return df

ET_Temp(df)

####### Data setup: ####### 

def data_setup(df):

    morning_sh = df.query('"06:50" < time < "08:34"') # query data associated with morning shower 

    evening_dish = df.query('"19:02" < time < "19:58"') # query data associated with evening dish washer

    evening_sh = df.query('"20:01" < time < "20:57"') # query data associated with evening shower

##### Get Cumulative Energy for each event ######

    df['cumsum_morning_sh'] = morning_sh['consumed_watts'].cumsum(axis=0)

    df['cumsum_evening_dish'] = evening_dish['consumed_watts'].cumsum(axis=0)

    df['cumsum_evening_sh'] = evening_sh['consumed_watts'].cumsum(axis=0)

###### Fill NaNs with zero ######

    df = df.fillna(0)

    return morning_sh, evening_dish, evening_sh, df

data_setup(df)

morning_sh,evening_dish,evening_sh,df = data_setup(df)



####### set the equation: (pay attention to units) ####### 

# Equation is COP = Q (btu/hr) / Net Energy (Wh) 
# Where Q = m_dot * cp * delta_t
# And Net Energy is the consumed_watts column

def cop_morning(morning_sh):
    
    rho = 62.4                                  # water density (lbm/cu ft)

    v_dot = 16.4                                # volumetric flow rate (cu ft/hr)

#m_dot = rho * v_dot                        # mass of the water in the tank (lbm/hr)

#m_dot = 10014                               # Assuming the draw is 20 gpm. Convert 20 gpm to lbm/hr

    m_dot = 415

    cp = 1.001                                  # water specific heat (btu/lbm.F)

    T_in = 75                                   # Temperature of the water in the tank (F) (maybe Ambient Temperature?)

    T_morning_sh = morning_sh['tank_temp']      # Temperature of the outlet water (F)

    T_evening_dish = evening_dish['tank_temp']  # Temperature of the outlet water (F)

    T_evening_sh = evening_sh['tank_temp']      # Temperature of the outlet water (F)

    Q_btu = m_dot * cp * (T_morning_sh - T_in)  # Heat in btu/hr

    Q_wh = Q_btu * 0.293                        # Heat in wh

    net_energy = df.query('"06:50" < time < "08:34"')

    net_energy = net_energy['cumsum'] -1443

    #net_energy = net_energy['consumed_watts'].cumsum()
    
    net_energy = net_energy.mean()

    #print('here is the mean of the real power values: ',net_energy)
    
    df['cop'] = Q_wh/net_energy

    return df                                   # cop values are included in the dataframe (morning shower evet only)

cop_morning(morning_sh)

cop = cop_morning(morning_sh)
cop.to_csv('try.csv')



df_morning = df.query('"06:50" < time < "08:06"')

df_dish = df.query('"19:06" < time < "19:55"')

df_evening_sh = df.query('"20:03" < time < "20:53"')

def plots(df2):   
    
    y = df2['cop']
    
    x = df2['tank_temp']

    fig = plt.figure(figsize=(12,8))
    
    ax = fig.add_subplot(111)
    
    ax.plot(x,y)
    
    ax.set_xlabel('Tank Temp [F]')
    
    ax.set_ylabel('COP')
    
    ax.set_title('HPWH COP (20 Gallon Water Draw)')

    plt.grid()

    plt.show()

plots(df_morning)

#p1 = [101.5,1.94]   #x,y
#p2 = [111,2.63]   #x,y

#font = {'family':'serif','color':'k','weight':'normal','style':'italic','size':12,}
#curlyBrace(fig,ax,p1,p2, k_r =0.05 ,str_text='Heating element ON',color='r',lw=3,int_line_num=1,fontdict=font)
#plt.annotate('Heating Element is Triggered',xy=('101.5','1.9'),xytext=(0,200),arrow)
#plt.show()
#plt.savefig('cop_sim.png')
print('done')
###### 



