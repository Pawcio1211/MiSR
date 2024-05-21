import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from time import time
import math

robot = rtb.models.Panda()
robot.q = robot.qz
x0=0.64
y0 = 0.2
z0 = 0.15
r = 0.1
probki = 50
x=[]
y=[]
z=[]
a=[]
b=[]
b.append(robot.qz)
kat = 2*math.pi/probki

for i in range(0,probki):
    x.append(x0+r*cos(kat*i))
    y.append(y0+r*sin(kat*i))
    a.append(robot.ikine_LMS(SE3(x[i],y[i],z0)*SE3.Rx(np.pi)))
    b.append(a[i].q)

plt.plot(x,y)
plt.show()
b.append(robot.qz)
via_pt=np.array(b)
traj=mstraj(via_pt, dt = 0.1, tacc = 0.02, qdmax = 2.0)
rtb.qplot(traj.q)
robot.plot(traj.q, backen = 'pyplot',move='panda_pyplot.gif')
