from roboticstoolbox.tools.trajectory import *
from roboticstoolbox.backends import Swift
from spatialmath.base.symbolic import *
from spatialmath.base import *
from spatialmath import SE3
from spatialmath import *
import matplotlib.pyplot as plt
import roboticstoolbox as rtb
import sympy as sym
import numpy as np
import spatialmath
import time


robot = rtb.models.Panda()


#dane
z = 0.15
x_o = 0.65
y_o = 0.2
r=0.1
ilosc_p = 60
step = 2*np.pi/ilosc_p

#pojemniki
x=[]
y=[]
ruch = []
ruch_z_q=[]

for i in range(ilosc_p):
    x.append(x_o+r*cos(i*step))
    y.append(y_o+r*sin(i*step))
   
    # print("x:",x[i],"   y:",x[i])

#plt.plot(x,y)
#plt.show()

#ruch.append(robot.qz)
ruch_z_q.append(robot.qz)
for i in range(ilosc_p):
    #print("...............................")
    ruch.append(robot.ikine_LMS(SE3(x[i],y[i],z)*SE3.OA([0,1,0],[0,0,-1])))
    print(ruch[i].q)
    if ruch[i].success is False:
        print("ruch[i].q = 0")
        break
    #print("...............................")
    ruch_z_q.append(ruch[i].q)

koniec=np.array(ruch_z_q)
traj = mstraj(koniec, dt=0.3, tacc=0.2, qdmax=2.0)
rtb.qplot(traj.q)

robot.plot(traj.q, backend='pyplot', movie='panda_pyplot.gif')