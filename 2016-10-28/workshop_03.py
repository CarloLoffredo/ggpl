from pyplasm import *

def ggpl_doubleRunStair(dx, dy, dz):
	""" 
	Creates a double run stair in a box defined by the parameters.
	
	@param dx: the x dimension of the box
	@param dy: the y dimension of the box
	@param dz: the z dimension of the box
	@return: the HPC object of the whole structure
	"""
	voidRiserHeight = 0.08	
	numRiser = dz/0.18
	
	xPlatform = min(0.31*dx,2)
	yPlatform = dy
	zPlatform = 0.18
	
	xRiser = (0.69*dx)/(numRiser/2)
	yRiser = dy/2.0 - 0.10
	zRiser = 0.18
	
	basePlatform = CUBOID([xPlatform,yPlatform,zPlatform-voidRiserHeight])
	baseRiser = CUBOID([xRiser,yRiser,zRiser-voidRiserHeight])
	
	height = 0
	xCoord = 0
	scene = STRUCT([CUBOID([0.01,0.01])])
	
	# placing the first run of risers
	for n in range(0,int(numRiser/2)):
		scene = STRUCT([scene,T([1,3])([xCoord,height]),baseRiser])
		xCoord = xCoord + xRiser
		height = height + zRiser
	
	# placing the platform
	scene = STRUCT([scene,T([1,3])([xCoord,height]),basePlatform])
	
	# placing the second run of risers
	height = height + zRiser
	xCoord = xCoord - xRiser
	for n in range(0,int(numRiser/2)):
		scene = STRUCT([scene,T([1,2,3])([xCoord,dy/2.0 + 0.10,height]),baseRiser])
		xCoord = xCoord - xRiser
		height = height + zRiser
	
	# raising the risers and the platform to the correct height
	scene = T([3])(voidRiserHeight)(scene)
	
	# placing the supporting wall
	suppWall = CUBOID([(int(numRiser/2))*xRiser,0.20,height])
	scene = STRUCT([scene,T(2)(dy/2.0 - 0.10),suppWall])
	
	
	print SIZE([1,2,3])(scene)
	
	# scaling the structure to the desired size
	sceneSize = SIZE([1,2,3])(scene)
	scene = S([1,2,3])([1/sceneSize[0],1/sceneSize[1],1/sceneSize[2]])(scene)
	scene = S([1,2,3])([dx,dy,dz])(scene)
	
	print SIZE([1,2,3])(scene)
	
	return scene

VIEW(ggpl_doubleRunStair(4,3,4))