import pygame
import numpy as np
# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")
screen.fill((0, 0, 0))
pygame.display.update()

#Grille
for i in range(0,800,20):
    pygame.draw.line(screen, 'white', (i,0), (i,600), width=1)
    pygame.display.update()
for j in range(0,600,20):
    pygame.draw.line(screen, 'white', (0,j), (800,j), width=1)
    pygame.display.update()
    
#Forme avec des lignes
for i in range(0,800,20):
    pygame.draw.line(screen,'red',(0,i),(i,600),width=1)
    pygame.display.update()

#Cercles
r=np.sqrt((800**2+600**2)/16)
"""Pour voir les centres des cercles apartient a ce cerlce"""
#pygame.draw.circle(screen, 'green', (800//2,600//2), r, width=2)
#pygame.display.update()

for i in range(0,100):
    r1=np.sqrt((800**2+600**2)/64)
    x=r*np.cos(i*np.pi/50)+800/2; y=600/2+r*np.sin(i*np.pi/50)
    pygame.draw.circle(screen, 'blue', (x,y), r1, width=1)
    pygame.display.update()

Running = True
# Main game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False