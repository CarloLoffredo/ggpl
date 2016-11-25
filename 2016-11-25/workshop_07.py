from pyplasm import *

#a = [[1,1,1,1,1],[1,-1,1,-1,1],[1,1,1,1,1],[1,-1,1,-1,1],[1,1,1,1,1]]
a = [[1,1,1,1,1],[1,-1,1,-1,1],[1,1,1,-1,1],[1,-1,1,-1,1],[1,-1,1,1,1],[1,-1,1,-1,1],[1,1,1,-1,1],[1,-1,1,-1,1],[1,1,1,1,1]]

x = [0.05,0.5,0.03,0.3,0.03,0.3,0.03,0.5,0.05]
z = [0.05,0.85,0.03,0.34,0.05]

X = QUOTE(x)

Z = QUOTE(z)

dx = 0

scene = CUBOID([0.01,0.01,0.01])

for i in range(0,len(a)):
	temp = [k*j for k,j in zip(z,a[i])]
	deepness = QUOTE([0.08])
	base = PROD([QUOTE([x[i]]),deepness])
	cell = PROD([base,QUOTE(temp)])
	scene = STRUCT([scene,T(1)(dx),cell])
	dx = dx + x[i]

#scene = OFFSET([0,0,0.08])(scene)

VIEW(scene)
