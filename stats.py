import numpy as np
import pandas as pd

df=pd.read_csv("forestfires.csv")

for col in df:
	print "mean ",col,np.mean(df[col])
	print "median",col,np.median(df[col])
	a=min(df[col])
	b=max(df[col])
	print "range",col," ",a,",",b
