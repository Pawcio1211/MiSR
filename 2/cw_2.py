import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from spatialmath.base.symbolic import *
from time import time
import math

#zad1
l1=symbol('l1')
l2=symbol('l2')
q1,q2,q3 = symbol('q1,q2,q3')

robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=l1, alpha= pi()/2),
        rtb.RevoluteDH(offset=pi()/2, alpha= pi()/2),
        rtb.PrismaticDH(offset=l2)
    ], name="My_Robot")
'''
print('Zad.1 tabelka:\n')
#print(robot.links[0])
#print(robot.links[1])
#print(robot.links[2])
#print('\n')
'''
#zad2
q = [q1,q2,q3]
T = robot.fkine(q)
#print(T)
#zad3
J=robot.jacob0(q)
Jsimple=simplify(J)
#print(Jsimple)
#zad 5
Puma =rtb.models.DH.Puma560()
T=Puma.fkine(Puma.qn)
print(T)