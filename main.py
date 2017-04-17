import pygame
from pygame.locals import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from math import *

background_vertices = (
	(1,1,0),
	(-1,1,0),
	(-1,-1,0),
	(1,-1,0)
	)

background_edges = (
	(0,1),
	(1,2),
	(2,3),
	(3,0)
	)

background_surfaces = (
	(0,1,2,3)
	)

background_colors = (
	(0.0,0.749019608,1),
	(0.0,0.5,0.8),
	(0.0,0.5,0.8),
	(0.0,0.749019608,1)
	)

def Background():
	glBegin(GL_LINES)
	for edge in background_edges:
		for vertex in edge:
			glVertex3fv(background_vertices[vertex])
	glEnd()

	glBegin(GL_QUADS)
	x = 0
	for vertex in background_surfaces:
		glColor3fv(background_colors[x])
		glVertex3fv(background_vertices[vertex])
		x += 1
	glEnd()

def Sun():
	posx = 0.7   
	posy = 0.7
	posz = 0   
	sides = 32
	radius = 0.15
	glBegin(GL_POLYGON)
	for i in range(100):
		cosine = radius * cos(i*2*pi/sides) + posx    
		sine = radius * sin(i*2*pi/sides) + posy    
		glColor3fv((1,1,0))
		glVertex3f(cosine,sine, posz)
	glEnd()

def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0,0.0, -5)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Background()
		Sun()
		pygame.display.flip()
		pygame.time.wait(10)

main()