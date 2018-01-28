#used for preparung data i.e. reading csv file
import pandas as pd
#plot figures
import matplotlib.pyplot as plt
import numpy as np
import math

#---------------------------------------------------------------------------------------
df  = pd.read_csv("forestfires.csv")
out=np.log(1+(df.area))
#df.loc[:,14] = pd.Series(df.loc[:,'out'], indedf[df.index)
df.plot()  # plots all columns against index
plt.show()
plt.scatter(df['X'],out) # scatter plot
plt.xlabel("X")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['Y'],out) # scatter plot
plt.xlabel("Y")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['month'],out) # scatter plot
plt.xlabel("month")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['day'],out) # scatter plot
plt.xlabel("day")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['FFMC'],out) # scatter plot
plt.xlabel("FFMC")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['DMC'],out) # scatter plot
plt.xlabel("DMC")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['DC'],out) # scatter plot
plt.xlabel("DC")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['ISI'],out) # scatter plot
plt.xlabel("ISI")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['temp'],out) # scatter plot
plt.show()
plt.scatter(df['RH'],out) # scatter plot
plt.xlabel("RH")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['wind'],out) # scatter plot
plt.xlabel("wind")
plt.ylabel("area")
plt.grid(True)
plt.show()
plt.scatter(df['rain'],out) # scatter plot
plt.xlabel("rain")
plt.ylabel("area")
plt.grid(True)
plt.show()
#df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram
