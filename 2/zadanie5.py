import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from time import time
import math

puma =rtb.models.DH.Puma560()
T=puma.fkine(puma.qn)

t1=time()
ik_a=puma.ikine_a(T)
t12=time()
elapsed1 = t1-t12
#print(ik_a)

t2 = time()
ik_LM = puma.ikine_LM(T)
t22 = time()
elapsed2 = t2-t22
#print(ik_LM)

t3 = time()
ik_LMS = puma.ikine_LMS(T)
t32 = time()
elapsed3 = t3-t32
#print(ik_LMS)

t4 = time()
ik_min_T = puma.ikine_min(T,qlim=True)
t42 = time()
elapsed4 = t4-t42
#print(ik_min_T)

t5 = time()
ik_min_F = puma.ikine_min(T,qlim=False)
t52 = time()
elapsed5 = t5-t52
#print(ik_min_F)

prosto=puma.fkine(ik_a.q)
roznica = T-prosto

blad_a = np.linalg.norm(roznica)
blad_LM = ik_LM.residual
blad_LMS = ik_LMS.residual
blad_min_T = ik_min_T.residual
blad_min_F = ik_min_F.residual


print('Czas ikine_a:  ',elapsed1)
print(blad_a)
print('\n')
print('Czas ikine_LM:  ',elapsed2)
print(blad_LM)
print('\n')
print(elapsed3)
print(blad_LMS)
print('\n')
print('Czas ikine_min_T:  ',elapsed4)
print(blad_min_T)
print('\n')
print('Czas ikine_min_F:  ',elapsed5)
print(blad_min_F)
print('\n')

bledy=[blad_a,blad_LM,blad_LMS,blad_min_T,blad_min_F]

print('zwyciezca jest maszyna z czasem: ',min(bledy))