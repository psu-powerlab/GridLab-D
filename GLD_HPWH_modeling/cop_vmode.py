import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import datetime as dt
from datetime import datetime
import matplotlib.dates as mdates
from scipy.integrate import quad
from scipy.integrate import trapz as tz
from curlyBrace import curlyBrace

path ='/home/parallels/Desktop/thesis_work/csv_files/hpwh_vmode_oct.csv'
#path ='/home/parallels/Desktop/thesis_work/csv_files/hpwh_no_load_up_emcb_closed.csv'


def wr(df):
    return df.to_csv('try.csv',index=False)

def prep_files(path):
    df = pd.read_csv(path)
    df['time'] = pd.to_datetime(df['timestamp']).dt.strftime('%H:%M')#.astype('datetime64') # Change time format for simplicity

    return df
'''
def avg_power(df):
    df['consumed_watts'] = df['consumed_watts'].round(2)
    #df['avergae_watts'] = (df['consumed_watts'].expanding(1).mean()).round(2)
    df = df.query('1 < consumed_watts < 600')
    df['avergae_watts'] = (df['consumed_watts'].rolling(1).mean()).round(2)
    return df

def cleaning(df):
    df = df.drop(['real_available_Wh'],axis=1)
    return df


def cop(df):
    watts = df['avergae_watts']
    energy = df['real_available_Wh']
    df['cop'] = (energy/watts).round(2)
    print('watts ----->\n',watts)
    print('EnergyTake ----->\n',energy)
    print('cop -------->\n',df['cop'])

    return df

def plots(df):

    x = df['real_available_Wh']
    y = df['cop']
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y)
    ax.set_xlabel('EnergyTake (Wh)')
    ax.set_ylabel('COP')
    ax.set_title('HPWH COP (Vacation Mode Recovery)')
    plt.grid()
    #plt.savefig('/home/parallels/Desktop/thesis_work/figures/cop_vs_EnergyTake.png')
    plt.show()

'''
def main(path):
    df = prep_files(path)
    df = df.drop_duplicates()
    #df = cleaning(df)
    #df = avg_power(df)
    #df = cop(df)
    wr(df)
    #df = plots(df)

main(path)

'''
def line_fit(df):

    x = df['real_available_Wh']
    #y = df['cop_heating_elem']
    y = df.query('9 > cop_heating_elem')
    m,b = np.polyfit(x,y,1)
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.plot(x,y,'o')
    ax.plot(x,m*x+b)

    ax.set_xlabel('EnergyTake (Wh)')
    ax.set_ylabel('COP')
    ax.set_title('HPWH COP (Vacation Mode Recovery)')
    plt.grid()
    #plt.savefig('/home/parallels/Desktop/thesis_work/figures/cop_vs_EnergyTake.png')
    plt.show()    

print('done')
#    df['time'] = df['time'].diff().astype('str').str.split('0 days ').str[-1]

#heating_elem_time = [i for i in range(1,len(df['consumed_watts'])+1)]
#heating_elem_time = sorted(heating_elem_time,reverse=False)
#df['heating_elem_index'] = heating_elem_time

def minutes_calc(df):
    
    #Calculate how long the heating element and the compressor were on. It then passes the values to convert from watts to watts-hour function
    #The function return df2 that only contains the HPWH data when it was consuming power.
    heating_elem = df.query('real_available_Wh > 75')
    # heating_elem = df.query('consumed_watts > 100')
    #heating_elem = df.query('consumed_watts > 4000')
    heating_elem_time = [i for i in range(1,len(heating_elem)+1)]
    heating_elem_time = sorted(heating_elem_time,reverse=True)
    heating_elem['heating_elem_index'] = heating_elem_time
    heating_elem['avg_Watts'] = heating_elem['consumed_watts'].rolling(window=len(heating_elem)).mean()


    comp = df.query('70 < real_available_Wh < 500')
    #comp = df.query('consumed_watts < 500')
    comp_time = [i for i in range(1,len(comp)+1)]
    comp_time = sorted(comp_time,reverse=True)
    comp['comp_index'] = comp_time
    df2 = heating_elem.append(comp)
    df2 = df2.fillna(0)
    
    df2['index'] = df2['heating_elem_index'] + df2['comp_index']
    df2 = df2.drop(['heating_elem_index','comp_index'],axis=1)

    return(heating_elem)

    #return df2
'''
    #cop_heating_elem['consumed_wh_heating_elem'] = (cop_heating_elem['consumed_watts'] *(cop_heating_elem['heating_elem_index']/76)).round(2)
    #cop_heating_elem['consumed_wh_heating_elem'] = (cop_heating_elem['consumed_watts'] *(cop_heating_elem['index']/60)).round(2)
    #cop_heating_elem['cop_heating_elem'] = (cop_heating_elem['real_available_Wh']/cop_heating_elem['consumed_wh_heating_elem']).round(2)
    #print((cop_heating_elem['cop_heating_elem']).mean())
    #cop_heating_elem['cop_heating_elem'] = cop_heating_elem.query(' 0 < cop_heating_elem < 7')

    #cop_comp = df2.query('consumed_watts < 600')
    #cop_comp['consumed_wh_comp'] = (cop_comp['consumed_watts'] * (cop_comp['index']/60)).round(2)
    #cop_comp['cop_comp'] = (cop_comp['real_available_Wh']/cop_comp['consumed_wh_comp']).round(2)

    #df2 = cop_heating_elem.append(cop_comp)
    #df2 = df2.fillna(0)
    #df2['cop'] = df2['cop_heating_elem'] + df2['cop_comp']
    #df2 = df2.drop(['cop_heating_elem','cop_comp'],axis=1)
    #print(df2['cop'].mean())