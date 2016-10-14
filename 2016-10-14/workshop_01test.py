from larlib import *
from random import randint

beamX = 1		# x dimension of beam section
beamZ = 1		# z dimension of beam section 

pillarX = 1		# x dimension of pillar section
pillarY = 1		# y dimension of pillar section
pillarZ = []		# z dimensions of pillars (interstory heights)
genericPillars = [] 	# list of generic pillars for each floor (different heights)

xPillarsNumb = 10	# number of pillars on the X axis
yPillarsNumb = 10	# number of pillars on the Y axis

floorNumb = 10		# number of floors

# now I'm generating interstory heights (pillarZ values)

t = 0
for i in range(0,floorNumb):
	next = randint(4,9) + t
	pillarZ.append(next)
	t = t + next

# now I'm generating the generic pillars for each floor
 
for m in range(0,floorNumb):
	newPillar = CUBOID([pillarX,pillarY,pillarZ[m]])
	genericPillars.append(newPillar)


# now I'm going to build the pillars

for n in range(0,floorNumb):
	for y in range(0,yPillarsNumb):
		if ((y == 0) & (n == 0)):
			scene = STRUCT([genericPillars[n]])				#building first pillar
		scene = STRUCT([scene,T(2)(5*y),T(3)(pillarZ[n]),genericPillars[n]])	#building the rest of the pillars

VIEW(scene)