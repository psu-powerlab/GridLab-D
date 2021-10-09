import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from random import randint

z = 0
T_amb = [] # ambient temperature
T_lw = [] # Leaving water temperature
T_w = [] # Water Temperature inside the tank
cop = [] # coefficient of performance values for each of the above values

# All temps in K

while z <= 200:
    amb = randint(-23,22)
    lw = randint(27,57)
    w = randint(37,49)
    T_amb.append(amb)
    T_lw.append(lw)
    T_w.append(w)
    z=z+1
'''
c1 = -0.0000069799987842105791
c2 = 0.004273691410554629
c3 = -0.65199966934276532
c4 = 0.0040140856414434441
c5 = -2.4623917638476516
c6 = 376.55576426211297
c7 = -0.57565417099277261
c8 = 353.64815505175926
c9 = -54179.724395432037



# cop equation from Barrett's thesis appendix A

i = 0
while i < len(T_amb):
    cop_eq = (c1 * (pow(T_amb[i],2)) * (pow(T_lw[i],2))) + (c2 * (pow(T_amb[i],2)) * T_lw[i]) + (c3 * (pow(T_amb[i],2))) + (c4 * T_amb[i] * (pow(T_w[i],2))) + (c5 * T_amb[i] * T_w[i]) + (c6 * T_amb[i]) + (c7 * (pow(T_w[i],2))) +(c8 * (pow(T_w[i],2))) + c9
    cop.append(cop_eq)
    i = i +1
print(cop)
#print(len(cop))i

#cop = c1 * (pow(T_amb,2)) * (pow(T_lw[i],2)) + c2* (pow(T_amb[i],2)) * T_lw[i] + c3* (pow(T_amb[i],2)) + c4 *T_amb[i] * (pow(T_w[i],2)) + c5 * T_amb[i] * T_w[i] + c6 * T_amb[i] + c7 * (pow(T_w[i],2)) +c8 * (pow(T_w),2) + c9



coeffs = np.polynomial.polynomial.polyfit(T_amb,T_lw,2)
print(coeffs)

# Results are not as expected. Weird COP values are given. Let's move to another equation ..

'''


