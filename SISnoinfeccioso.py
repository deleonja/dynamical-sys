from sympy import *
from sympy.abc import S,I,t,b,g

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

b=1
g=1
def dx_dt(x,t):
    return [ -b*x[0]+g*x[1] , b*x[0]-g*x[1] ]
#trayectorias en tiempo hacia adelante
ts=np.linspace(0,10,500)
ic=np.linspace(20000,100000,3)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"-", color="orangered", lw=1.5)
#trayectorias en tiempo hacia atras
ts=np.linspace(0,-10,500)
ic=np.linspace(20000,100000,3)
for r in ic:
    for s in ic:
        x0=[r,s]
        xs=odeint(dx_dt,x0,ts)
        plt.plot(xs[:,0],xs[:,1],"-", color="orangered", lw=1.5)
#etiquetas de ejes y estilo de letra
plt.xlabel('S',fontsize=20)
plt.ylabel('I',fontsize=20)
plt.tick_params(labelsize=12)
plt.ticklabel_format(style="sci", scilimits=(0,0))
plt.xlim(0,100000)
plt.ylim(0,100000)
#campo vectorial
X,Y=np.mgrid[0:100000:15j,0:100000:15j]
u=-b*X+g*Y
v=b*X-g*Y
pl.quiver(X,Y,u,v,color='dimgray')
plt.savefig("SIS.pdf",bbox_inches='tight')
plt.show()