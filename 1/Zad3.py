import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
#-----------------------
# 3.1
#-----------------------
'''
dp = [1, -2, 2]

tbs = [2, 5, 0]

tps = [3,- 6, 4]

Rbs = np.array([[0,-1,0],[1,0,0],[0,0,1]])

Rps = np.array([[-1,0,0],[0,1,0],[0,0,-1]])
ds=Rps.transpose() @ dp -(Rps.transpose() @ tps)
print(ds)
db=Rbs@ds+tbs
print(db)
'''
#-----------------------
# 3.2
#-----------------------
dp = SE3(1,-2,2)
tbs = SE3(2,5,0)
tps = SE3(3,-6,4)
Rbs = SE3.Rz(90,'deg')
Rps = SE3.Ry(180,'deg')
B = SE3(0,0,0)
S = B*(tbs*Rbs)
P = S*(tps*Rps).inv()

B.plot(frame = 'B', color='blue', width = 10)
S.plot(frame = 'S', color='yellow', width = 10)
P.plot(frame = 'P', color='green', width = 10)

Tsp = (tps*Rps).inv() 
ds = Tsp*dp
Tbs = (tbs*Rbs)
db=Tbs*ds

plt.quiver(B.A[0,3],B.A[1,3],B.A[2,3],tbs.A[0,3],tbs.A[1,3],tbs.A[2,3])
plt.quiver(B.A[0,3],B.A[1,3],B.A[2,3],db.A[0,3],db.A[1,3],db.A[2,3])

plt.show()


