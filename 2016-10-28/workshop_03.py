from pyplasm import *

def ggpl_doubleRunStair(dx, dy, dz):
	
	numRaiser = dz/0.18
	
	xPlatform = min(0.31*dx,2)
	yPlatform = dy
	zPlatform = 0.18
	
	xRaiser = (0.69*dx)/(numRaiser/2)
	yRaiser = dy/2.0 - 0.10
	zRaiser = 0.18
	
	basePlatform = CUBOID([xPlatform,yPlatform,zPlatform-0.12])
	baseRaiser = CUBOID([xRaiser,yRaiser,zRaiser-0.12])
	
	height = 0
	xCoord = 0
	scene = STRUCT([CUBOID([0.01,0.01])])
	
	# placing the first run of raisers
	for n in range(0,int(numRaiser/2)):
		scene = STRUCT([scene,T([1,3])([xCoord,height]),baseRaiser])
		xCoord = xCoord + xRaiser
		height = height + zRaiser
	
	# placing the platform
	scene = STRUCT([scene,T([1,3])([xCoord,height]),basePlatform])
	
	# placing the second run of raisers
	height = height + zRaiser
	xCoord = xCoord - xRaiser
	for n in range(0,int(numRaiser/2)):
		scene = STRUCT([scene,T([1,2,3])([xCoord,dy/2.0 + 0.10,height]),baseRaiser])
		xCoord = xCoord - xRaiser
		height = height + zRaiser
	
	# raising the raisers and the platform to the correct height
	scene = T([3])(0.12)(scene)
	
	# placing the supporting wall
	suppWall = CUBOID([0.69*dx - (xRaiser/2),0.20,dz + 0.06])
	scene = STRUCT([scene,T(2)(dy/2.0 - 0.10),suppWall])
	
	
	print SIZE([1,2,3])(scene)
	
	# scaling the structure to the desired size
	sceneSize = SIZE([1,2,3])(scene)
	scene = S([1,2,3])([1/sceneSize[0],1/sceneSize[1],1/sceneSize[2]])(scene)
	scene = S([1,2,3])([dx,dy,dz])(scene)
	
	print SIZE([1,2,3])(scene)
	
	return scene

VIEW(ggpl_doubleRunStair(3,3,3))