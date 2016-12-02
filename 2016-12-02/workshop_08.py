import csv
import sys

from pyplasm import *

lines = []
line = []
A = []
B = []

f = open('wireframe.lines', 'rt')
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
    newline = MKPOL([[A,B],[[1,2]],[1]])
    scene = STRUCT([scene,newline])
    A = []
    B = []

scene = OFFSET([3,3,35])(scene)

sceneSize = SIZE([1,2,3])(scene)
scene = S([1,2,3])([1/sceneSize[0],1/sceneSize[1],1/sceneSize[2]])(scene)
scene = S([1,2,3])([35,50,3])(scene)

VIEW(scene)