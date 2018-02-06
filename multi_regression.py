import pandas as pd
import numpy as np
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

df= pd.read_csv("forestfires.csv")
out=np.log(1+(df.area))
#------------------------------------------------------------------------------------
model = smf.ols(formula='out ~ X+Y+month+day+FFMC+DMC+DC+ISI+temp+RH+wind+rain', data=df).fit()
print model.summary()

#null hypothesis rejected for month and DC
'''
x_surf, y_surf = np.meshgrid(np.linspace(df2.X.min(), df2.X.max(), 100),np.linspace(df2.month.min(), df2.month.max(), 100))
onlyX = pd.DataFrame({'X': x_surf.ravel(), 'month': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df2['X'],df2['month'],df2['out'],c='blue', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='None', alpha=0.01)
ax.set_xlabel('X')
ax.set_ylabel('month')
ax.set_zlabel('out')
plt.show()
'''

