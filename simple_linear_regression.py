import numpy as np
import pandas as pd
from datetime import datetime
from pandas import Series, DataFrame
import statsmodels.api as sm

df=pd.read_csv("forestfires.csv")

#------------------------------------------------------------------------------------------------------
	
for col in df:
	df1 = pd.DataFrame(df[col])
	target = pd.DataFrame(df["area"])
	X = df1
	y = target
	model = sm.OLS(y, X).fit()
	predictions = model.predict(X) # make the predictions by the model
	# Print out the statistics
	print model.summary()

