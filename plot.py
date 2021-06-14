import matplotlib.pyplot as plt
import numpy as np
import random
# (0,0),(0,1),(1,1),(1,0),(0,0),(.5,.5),(0,1),(1,1),(.5,.5),(1,0)
# (0,0),(0,1),(1,1),(1,0),(0,0)
#(0,0),(2,0),(1,2.75),(0,0),(1,1),(1,2.75),(2,0),(1,1)
#(0,0),(2,0),(1,2.75),(0,0)
xtricenter = [0,2,1,0,1,1,2,1]
ytricenter=[0,0,2.75,0,1,2.75,0,1]
xsquare=[0,0,1,1,0]
ysquare = [0,1,1,0,0]
xqaudcenter = [0,0,1,1,0,.5,0,1,.5,1]
yquadcenter=[0,1,1,0,0,.5,1,1,.5,0]
xtriangle = [0,2,1,0]
ytriangle = [0,0,2.75,0]
xcube = [0,0,1,1,0,1,1.5,1.5,1,0,.5,1.5,1,1,0,.5,1.5,1.5,.5,.5]
ycube = [0,1,1,0,0,0,.5,1.5,1,1,1.5,1.5,1,0,0,.5,.5,1.5,1.5,.5]
x=xcube
y=ycube
xpoints = np.array(x)
ypoints = np.array(y)
plt.plot(xpoints, ypoints,marker='o',c='hotpink')
plt.grid(color = 'blue', linestyle = 'dotted', linewidth = 0.75)
plt.show()
