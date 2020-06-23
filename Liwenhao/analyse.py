import pandas as pd
import numpy as np

pd.set_option('display.max_columns',None)

df = pd.read_csv('data/HSI.csv', header=0)
print(df.dtypes)

df['chazhi'] = df['OptionID'] - df['Strike']
print(df['chazhi'].min())
