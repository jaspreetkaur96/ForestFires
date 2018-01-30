import numpy as np
import pandas as pd
from prettytable import PrettyTable

df=pd.read_csv("forestfires.csv")

def IQR(col):
    return np.percentile(df[col], 75) - np.percentile(df[col], 25)

#------------------------------------------------------------------------------------------------------
t = PrettyTable(['Mean', 'Median','Min','Max','1st Quar','3rd Quar','IQR'])

	t.add_row([np.mean(df[col]),np.median(df[col]),min(df[col]),max(df[col]),np.percentile(df[col],25),np.percentile(df[col],75),IQR(col)])
print t
