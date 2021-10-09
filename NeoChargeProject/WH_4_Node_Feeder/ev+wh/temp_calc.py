from scipy import misc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wh_1.csv',usecols=['heatgain'])
df1 = pd.read_csv('wh_1.csv',usecols=['temperature'])
heatgain = df['heatgain'].tolist()
twt = df1['temperature'].tolist()                   #Tank water temperature and ambient temperature

####################################################
'''
th = Tank Heat
CL = Convection Loss
RL = Radiation Loss
dt = delta temperature
at = ambient temperature
tsa = total surface area
i_f = insulation factor
'''

def convection_loss(x,y):
    return (0.3 * ((x-y)**0.25))
def delta(x,y):
    return (x - y)
def radiation_loss(x,y):
    ft = (((x+460)/100)**4)                       #First Term
    st = (((y+460)/100)**4)                       #second term
    diff = ft - st
    return ((0.14 * (ft - st))/(delta(x,y)))

def tank_heat(x,y,tsa,i_f):
    t_h = (convection_loss(x,y) + radiation_loss(x,y)) * delta(x,y) * tsa * i_f
    return t_h
heat = []
k = 1 
i = 0
while k < 2900:
    r = twt[k]
    while i < k:
        v = twt[i]
        if v == r:
            heat.append(1)
        else:
            b = tank_heat(v,r,29.22,0.11)
            heat.append(b)
        i = i + 1
    k = k + 1
for l in heat:
    print(l)
