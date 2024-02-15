import pygame 
from src.classes.shapes import Rect
import os
from config import pieces,size,arr2d
import chess



fen = 'r6k/pp2r2p/4Rp1Q/3p4/8/1N1P2R1/PqP2bPP/7K b - - 0 24'

board = chess.Board(fen)
pygame.init() 


color = (255,255,255) 
position = (0,0) 

# CREATING CANVAS 
canvas = pygame.display.set_mode((8*size,8*size)) 

# TITLE OF CANVAS 
pygame.display.set_caption("Chess")



list_of_objs = list()

for i in range(8):
	for j in range(8):
		if (i+j)%2==0:
			list_of_objs.append(Rect(size,size,i*size,j*size,(255,255,255)))
		else:
			list_of_objs.append(Rect(size,size,i*size,j*size,(150,150,150)))


pyimgs = dict()

for k,v in pieces.items():
	pyimgs[k] = pygame.image.load('./src/assets/chessp/'+v).convert_alpha()
	pyimgs[k] = pygame.transform.scale(pyimgs[k],(size,size))


ap = list()
# pos = arr2d(board.__str__())
# for i in range(8):
# 	for j in range(8):
# 		if pos[i][j]!= '.':
# 			canvas.blit(pyimgs[pos[i][j]],(j*size,i*size))


exit = False
while not exit: 
	canvas.fill(color)
	for i in list_of_objs:
		i.draw(canvas)
	pos = arr2d(board.__str__())
	for i in range(8):
		for j in range(8):
			if pos[i][j]!= '.':
				canvas.blit(pyimgs[pos[i][j]],(j*size,i*size))
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True

	pygame.display.update() 
