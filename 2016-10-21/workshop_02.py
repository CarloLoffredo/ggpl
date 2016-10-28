from larlib import *
from random import randint


def frame(bx, bz, px, py, beam_Y, pillar_Z):

	beamX = bx		# x dimension of beam section
	beamZ = bz		# z dimension of beam section 
	beamY = beam_Y		# distances between axes of the pillars
	
	pillarX = px		# x dimension of pillar section
	pillarY = py		# y dimension of pillar section
	pillarZ = pillar_Z	# interstory heights

	frame = STRUCT([CUBOID([0.01,0.01,0.01])])
	height = 0
	
	# First, building the pillars
	
	for h in range(0,len(pillarZ)):
		a = []
	
		for i in range(0,len(beamY)):
			a.append(py)
			a.append(-beamY[i]+py)
		a.append(py)
	
		A = QUOTE(a)
		B = QUOTE([px])
		C = PROD([A,B])
		H = QUOTE([pillarZ[h]])
		D = PROD([C,H])
		frame = STRUCT([frame,T(3)(height),D])
		height = height + pillarZ[h] + bz
	
	
	# Then, building the beams
	
	height = 0
	
	for h in range(0,len(pillarZ)):
		a = []
		height = height + pillarZ[h]
		for i in range(0,len(beamY)):
			if (i == len(beamY) - 1):
				a.append(beamY[i] + py)
			else:
				a.append(beamY[i])
	
		A = QUOTE(a)
		B = QUOTE([bx])
		C = PROD([A,B])
		H = QUOTE([bz])
		D = PROD([C,H])
		frame = STRUCT([frame,T(3)(height),D])
		height = height + bz
	
	return frame
	
def beams(frameParams):
	
	beamX = frameParams[1][0]		# x dimension of beam section
	beamZ = frameParams[1][1]		# z dimension of beam section 
	beamY = frameParams[2]			# distances between axes of the pillars
	
	pillarY = frameParams[1][3]
	pillarZ = frameParams[3]		# interstory heights
	height = 0
	
	newBeamLenght = frameParams[0][0]
	beams = STRUCT([CUBOID([0.01,0.01,0.01])])
	
	# Build the interconnecting beams
	
	for h in range(0,len(pillarZ)):
		a = []
		height = height + pillarZ[h]
		for i in range(0,len(beamY)):
			a.append(pillarY)
			a.append(-beamY[i]+pillarY)
		a.append(pillarY)
		
		A = QUOTE(a)
		B = QUOTE([newBeamLenght])
		C = PROD([A,B])
		H = QUOTE([beamZ])
		D = PROD([C,H])
		
		beams = STRUCT([beams,T(3)(height),D])
		height = height + beamZ
	
	return beams
	
	

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

	scene = STRUCT([CUBOID([0.001,0.001,0.001])])
	
	distance = 0
	
	# now building placing frames in scene
	
	for i in range(0,len(listFrames)):
		# update the vector
		distance = distance + listFrames[i][0][0]
		# build new frame
		newFrame = frame(listFrames[i][1][0],listFrames[i][1][1],listFrames[i][1][2],listFrames[i][1][3],listFrames[i][2],listFrames[i][3])
		# place new frame in scene
		scene = STRUCT([scene,T(2)(distance),newFrame])
	
	
	
	distance = listFrames[0][1][2]
	
	# now building and placing connecting beams
	for i in range(0,len(listFrames)):
		# build the connecting beams structure
		newBeams = beams(listFrames[i])
		# place new connecting beams in scene
		scene = STRUCT([scene,T(2)(distance),newBeams])
		# update the vector
		distance = distance + listFrames[i][0][0]
	
	
	#return scene
	return scene

VIEW(ggpl_bone_structure("frame_data_000001.csv"))