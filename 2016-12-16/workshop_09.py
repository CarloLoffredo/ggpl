import csv
import sys

from pyplasm import *

lines = []
line = []
A = []
B = []
C = []

f = open('perimetro.lines', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        for a in row:
            line.append(float(a))
        lines.append(line)
        line = []
finally:
    f.close()

scene = CUBOID([0.0001,0.0001,0.0001])
scene = DIFFERENCE([scene,scene])

for row in lines:
    A.append(row[0])
    A.append(row[1])
    B.append(row[2])
    B.append(row[3])
    C.append(row[2])
    C.append(row[3])
    C.append(3.0)
    newline = MKPOL([[A,B],[[1,2]],[1]])
    A.append(0.0)
    B.append(0.0)
    newplane = PLANE([A,B,C])
    newplane = R([1,3])(PI/4)(newplane[2])
    scene = STRUCT([scene,newline,newplane])
    A = []
    B = []
    C = []

sceneSize = SIZE([1,2,3])(scene)
scene = S([1,2,3])([1/sceneSize[0],1/sceneSize[1],1/sceneSize[2]])(scene)
scene = S([1,2,3])([35,35,1])(scene)

VIEW(scene)