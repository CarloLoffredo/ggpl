from larlib import *
from random import randint


def frame(bx, bz, px, py, beam_Y, pillar_Z):
	beamNumb = 9		# number of beams
	#pillarsNumb = 10	# number of pillars

	beamX = bx		# x dimension of beam section
	beamZ = bz		# z dimension of beam section 
	beamY = beam_Y		# distances between axes of the pillars
	beams = []		#list of beams

	pillarX = px		# x dimension of pillar section
	pillarY = py		# y dimension of pillar section
	pillarZ = pillar_Z	# interstory heights
	pillars = []

	"""
	CODE NOT WORKING CORRECTLY
	
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
	pillarDistance = 0
	beamDistance = 0
	# building pillars and beams

	for n in range(0,len(pillars)):
		for m in range(0,len(beams)-1):
			pillar
			scene = STRUCT([scene,T(2)(pillarDistance[m]),T(3)((beamDistance[n])-pillarZ[n]),pillars[n]])
			scene = STRUCT([scene,T(2)(pillarDistance[m]),T(3)(beamDistance[n]),beams[m+1]])

		scene = STRUCT([scene,T(2)(pillarDistance[len(beams)-1]),T(3)((beamDistance[n])-pillarZ[n]),pillars[n]])
	"""
	
	# First, building the pillars
	
	a = []
	
	for i in range(0,len(beamY)):
		a.append(py)
		a.append(-beamY[i]+py)
	a.append(py)
	
	A = QUOTE(a)
	B = QUOTE([px])
	C = PROD([A,B])
	H = QUOTE([pillarZ[0]])
	D = PROD([C,H])
	
	
	# Then, building the beams
	

	
	return D
	

def ggpl_bone_structure(file_name):
	
	i = 0
	j = 0
	in_file = open(file_name, 'r')
	listFrames = [[]] 	# list of all frame parameters; each element is a list of parameters
	
	# parsing works correctly
	for line in in_file:
		
		line = line.rstrip('\n')
		
		if (i % 2 == 0):
			listFrames.append([])
			vector = line.split(" ")
			listFrames[j].append(vector)
		else:
			lineSplit = line.split(",")
			beamPillDims = lineSplit[0].split(" ")
			pillDist = lineSplit[1].split(" ")
			beamDist = lineSplit[2].split(" ")
			print j
			listFrames[j].append(beamPillDims)
			listFrames[j].append(pillDist)
			listFrames[j].append(beamDist)
			j = j + 1


		i = i + 1
	
	listFrames.pop()


	for i in range(0,len(listFrames)):
		for j in range(0,len(listFrames[i])):
			for n in range(0,len(listFrames[i][j])):
				listFrames[i][j][n] = float(listFrames[i][j][n])

	#for i in range(0,len(listFrames)):
	#	print listFrames[i]
	
	#scene = frame(listFrames[0][1][0],listFrames[0][1][1],listFrames[0][1][2],listFrames[0][1][3],listFrames[0][3],listFrames[0][2])

	scene = STRUCT([CUBOID([1,1,1])])
	
	distance = 0
	
	# now building placing frames in scene
	for i in range(0,len(listFrames)):
		# update the vector
		distance = distance + listFrames[i][0][0]
		# build new frame
		# TODO: function frame() does not work correctly (yet)
		newframe = frame(listFrames[0][1][0],listFrames[0][1][1],listFrames[0][1][2],listFrames[0][1][3],listFrames[0][3],listFrames[0][2])
		# place new frame in scene
		scene = STRUCT([scene,T(2)(distance),newframe])
	
	# now building and placing connecting beams
	# TODO
	
	return scene

VIEW(ggpl_bone_structure("frame_data_000000.csv"))