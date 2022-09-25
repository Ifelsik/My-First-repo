import matplotlib.pyplot as mpl
import numpy as np
x=np.linspace(0, 10,50)
y=[i**2 for i in x]
mpl.grid()
mpl.plot(x,y)
mpl.show()