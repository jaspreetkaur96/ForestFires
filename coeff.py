#used for preparung data i.e. reading csv file
import pandas as pd
#plot figures
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm

#---------------------------------------------------------------------------------------
df  = pd.read_csv("forestfires.csv")
out=np.log(1+(df.area))
model1 = smf.ols(formula='out ~ X+Y+month+day+FFMC+DMC+DC+ISI+temp+RH+wind+rain', data=df).fit()
#print model1.summary()
print model1.params
x = []
y=[]

for col in df:
	model2 = sm.OLS(pd.DataFrame(out), pd.DataFrame(df[col])).fit()
	print model2.params
	if col=="area":
		continue
   	x.append(model1.params[col])
   	y.append(model2.params)
plt.scatter(x,y)
plt.xlabel("SIMPLE LINEAR REGRESSION")
plt.ylabel("MULTIPLE LINEAR REGRESSION")
plt.grid(True)
for i,col in enumerate(df):
	if col=="area":
		continue	
	plt.annotate(col, (x[i],y[i]))
plt.show()

#df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram
'''

	df1 = pd.DataFrame(df[col])
	target = pd.DataFrame(out)
	X = df1
	y = target'''
