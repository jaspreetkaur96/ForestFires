import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#-----------------------------------------------------------------
df  = pd.read_csv("forestfires.csv")
out=np.log(1+(df.area))

for col in df:
	x = np.array(df[col])
	y = np.array(out)
	z=np.polyfit(x,y,3)
	p = np.poly1d(z)
	x_new = np.linspace(x[0], x[-1], 50)
	y_new = p(x_new)
	plt.plot(x,y,'o', x_new, y_new)
	plt.show()
