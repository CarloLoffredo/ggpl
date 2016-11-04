def ggpl_flat_top_roof(vertices,cells):
	
	# verify that the cells' vertices are complanar
	
	# the flat top is the 3rd cell
	flat_top = cells[2]
	
	# build the roof base model
	roof = MKPOL([vertices,cells,[]])
	
	# compute the 1-skeleton of the roof
	skelRoof = SKEL_1(roof)
	
	# place the faces, oriented upwards
	faces = MKPOL([vertices,cells, [] ])
	facesOff = OFFSET([0.05,0.05,0.05])(faces)
	
	# generate the roof frame using OFFSET() 
	frameRoof = OFFSET([0.2,0.2,0.2])(skelRoof)
	
	return STRUCT([frameRoof,facesOff])

from pyplasm import *

VIEW(ggpl_flat_top_roof([ [0,0,0], [0,20,0], [10,20,0], [10,0,0], [5,4,4], [5,16,4], [5,12,4], [17,12,4], [10,9,0], [20,9,0], [20,15,0], [10,15,0]],[ [1,4,5], [1,5,6,2], [2,6,3], [5,4,9,7], [6,7,12,3], [7,9,10,8], [7,8,11,12], [8,10,11] ]))