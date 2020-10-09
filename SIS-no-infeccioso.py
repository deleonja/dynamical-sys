# SIS not infectous model
# Author: José Alfredo de León
# 09.10.2020

# Program 03b: Nonlinear system, phase portrait with vector plot.
# See Figure 3.12.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import pylab as pl

beta = 1
gamma = 1
# The 2-dimensional nonlinear system.
def dx_dt(x, t):
    return [-beta*x[0] + gamma*x[1], beta*x[0] - gamma*x[1]]
# Trajectories in forward time.
ts = np.linspace(0, 10, 1000)
ic = np.linspace(-5, 5, 10)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:,0], xs[:,1], "r-")

# Trajectories in backward time.
ts = np.linspace(0, -10, 1000)
ic = np.linspace(-5, 5, 10)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        plt.plot(xs[:,0], xs[:,1], "r-")

# Label the axes and set fontsizes.
plt.xlabel("S", fontsize=12)
plt.ylabel("I", fontsize=12)
plt.tick_params(labelsize=10)
plt.xlim(-5, 5)
plt.ylim(-5, 5);

# Plot the vectorfield.
X, Y = np.mgrid[-5:5:12j, -5:5:12j]
u = -beta*X + gamma*Y
v = beta*X - gamma*Y
pl.quiver(X, Y, u, v, color = 'b')
plt.savefig('SIS-no-infeccioso.pdf')
