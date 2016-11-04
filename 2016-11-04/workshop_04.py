def ggpl_flat_top_roof(vertices,cells):
	
	# verify that the cells' vertices are complanar
	
	# the flat top is the 3rd cell
	flat_top = cells[2]
	
	# build the roof base model
	roof = MKPOL([vertices,cells,[]])
	
	# compute the 1-skeleton of the roof
	skelRoof = SKEL_1(roof)
	
	# build the jack and common rafters
	x = vertices[2][0]
	y = vertices[0][1]
	raftDist = 1.5
	xRaftNum = int(x/1.5) + 1.0
	yRaftNum = int(y/1.5) + 1.0
	
	xRaftDist = x/xRaftNum
	yRaftDist = y/yRaftNum
	
	# "south" rafters
	xPos = 0
	for n in range(0,int(xRaftNum)+1):
		rafter = MKPOL([ [[xPos,0,0],[xPos,min(vertices[7][1], (xPos/vertices[7][0])*vertices[7][1], ((xPos-vertices[6][0])/(x-vertices[6][0]))*(-vertices[6][1]) + vertices[6][1]),min(vertices[7][2],(xPos/vertices[7][0])*vertices[7][1], ((xPos-vertices[6][0])/(x-vertices[6][0]))*(-vertices[6][2]) + vertices[6][2])]] , [[1,2]] , [] ])
		skelRoof = STRUCT([skelRoof,rafter])
		xPos = xPos + xRaftDist

	"""
	Building the rafters for all four faces is going to be quite long and tedious.
	I need to find another method to build them more efficiently.
	"""
	
	# generate the roof frame using OFFSET() 
	frameRoof = OFFSET([0.2,0.2,0.2])(skelRoof)
	
	return frameRoof

from pyplasm import *

VIEW(ggpl_flat_top_roof([[0,9,0],[12,9,0],[12,0,0],[0,0,0],[3,6,3],[9,6,3],[9,3,3],[3,3,3]],[[1,2,6,5],[2,3,7,6],[5,6,7,8],[3,4,8,7],[1,5,8,4]]))