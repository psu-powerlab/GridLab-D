import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('house_meterControlled_30sec.xls',usecols=['#timestamp'])
print(df1)
