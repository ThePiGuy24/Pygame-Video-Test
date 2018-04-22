import pygame
from random import randint
import os
import time
try:
	import psutil
	Exit = False
except:
	print('please install the psutil library')
	Exit = True

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

frames = []

os.system('cls')
print('Starting...')
pygame.init()

mainFont = pygame.font.Font(None, 16)
dispOut = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

pygame.display.set_caption('VideoTest')

def dispText(msg,color,posy,posx):
	textOut = mainFont.render(msg, True, color)
	dispOut.blit(textOut, [posx, posy])

process = psutil.Process(os.getpid())

directory = os.listdir('frames/')
for file in directory:
	if file.endswith('.png'):
		frames.append(pygame.image.load('frames/'+file))
		print(file+' Successfully loaded.')
		dispOut.fill(black)
		dispText(str(round(process.memory_info()[1]/(1024*1024),1)) + "MB in use",white,0,0)
		pygame.display.update()
print(os.getpid())
	
while not Exit:
	timer = time.time()
	for frame in frames:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Exit = True
				print('Closing...')
		dispOut.blit(frame, [0,0])
		dispText(str(round(process.memory_info()[1]/(1024*1024),1)) + "MB in use",white,0,0)
		clock.tick(30)
		pygame.display.update()
	print(int((1/(time.time()-timer))*len(frames)))
		

pygame.quit()
os.system('cls')
quit()