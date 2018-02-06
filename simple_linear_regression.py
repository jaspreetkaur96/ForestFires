#https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9
#df in O/P-degree of freedom
import numpy as np
import pandas as pd
from pandas import tseries, DataFrame
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("forestfires.csv")

#------------------------------------------------------------------------------------------------------
out=np.log(1+(df.area))

for col in df:
	df1 = pd.DataFrame(df[col])
	target = pd.DataFrame(out)
	X = df1
	y = target
	model = sm.OLS(y, X).fit() #ordinary least squares
	predictions = model.predict(X) # make the predictions by the model
	# Print out the statistics
	print model.summary()

'''	lm = linear_model.LinearRegression()
	model = lm.fit(X,y)
	predictions = lm.predict(X)
	print predictions
	print lm.score(X,y)
	print lm.coef_
	print lm.intercept_

	'''


	
