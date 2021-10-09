import pandas as pd

path ='/home/parallels/Desktop/thesis_work/csv_files/hpwh_vmode.csv'

df = pd.read_csv(path)


df = df.drop(['idk','idk2','rated_real_power','idk3','max_watts_hour','idk4','idk5','idk6','op_state'],axis=1) 

df = df.query('5 < consumed_watts < 5000')

df = df.to_latex(index=False,longtable=True)
