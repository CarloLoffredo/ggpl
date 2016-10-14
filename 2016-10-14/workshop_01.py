from larlib import *
from random import randint

beamNumb = 10		# number of beams
#pillarsNumb = 10	# number of pillars

beamX = 1		# x dimension of beam section
beamZ = 1		# z dimension of beam section 
beamY = [3,5,4,6,3,5,4,6,3,5]		# distances between axes of the pillars
beams = []		#list of beams

pillarX = 1		# x dimension of pillar section
pillarY = 1		# y dimension of pillar section
pillarZ = [5,4,6,7,5,6,4,5,6,5]		#interstory heights
pillars = []

# calculate pillar axis distance from (0,0)
pillarDistance = [beamY[0]]
for i in range(1,len(beamY)):
	pillarDistance.append(sum(beamY[0:i+1]))

# calculate beam axis distance from (0,0)
beamDistance = [pillarZ[0]]
for j in range(1,len(beamY)):
	beamDistance.append(sum(pillarZ[0:j+1]))

# building all the beam types
for n in range(0,len(beamY)):
	beam = CUBOID([beamX,beamY[n],beamZ])
	beams.append(beam)


# building all the pillar types
for p in range(0,len(pillarZ)):
	pillar = CUBOID([pillarX,pillarY,pillarZ[p]])
	pillars.append(pillar)

#for n in range(0,len(pillarZ)):
#	beams.append(CUBOID([beamX,beamY[n],beamZ]))


scene = STRUCT([CUBOID([1,1,1])])

# building pillars and beams

for n in range(0,len(pillars)):
	for m in range(0,len(beams)-1):

		scene = STRUCT([scene,T(2)(pillarDistance[m]),T(3)((beamDistance[n])-pillarZ[n]),pillars[n]])
		scene = STRUCT([scene,T(2)(pillarDistance[m]),T(3)(beamDistance[n]),beams[m+1]])

	scene = STRUCT([scene,T(2)(pillarDistance[len(beams)-1]),T(3)((beamDistance[n])-pillarZ[n]),pillars[n]])
	

VIEW(scene)

	
