#used for preparung data i.e. reading csv file
import pandas as pd
#plot figures
import matplotlib.pyplot as plt
import numpy as np


#---------------------------------------------------------------------------------------
df  = pd.read_csv("forestfires.csv")
out=np.log(1+(df.area))
#df.loc[:,14] = pd.Series(df.loc[:,'out'], indedf[df.index)
df.plot()  # plots all columns against index
plt.show()

for col in {"X","Y","month","day","FFMC","DMC","DC","ISI","temp","RH","wind","rain"}:
	plt.scatter(df[col],out)
	plt.xlabel("col")
	plt.ylabel("area")
	plt.grid(True)
	plt.show()

#df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram
