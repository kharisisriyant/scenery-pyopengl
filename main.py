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

mountain_vertices = (
	(-1,0,0),
	(-0.5,0.75,0),
	(0,0,0),
	(0.5,0.75,0),	
	(1,0,0)
	)

mountain_edges = (
	(0,1),
	(1,2),
	(2,3),
	(3,4),
	(4,0)
	)

background_surfaces = (
	(0,1,2,3)
	)

road_vertices = (
	(0.5,0,0),
	(0,-2,0),
	(0.4,0,0),
	(-2,-1.75,0)
	)

road_edges = (
	(0,1),
	(2,3)
 )

background_colors = (
	(0.8,0.9,1),
	(0.4,0.69,1),
	(0.2,0.44,0.7),
	(0,0.34,0.7)
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

def Mountain():
	glBegin(GL_LINES)
	for edge in mountain_edges:
		for vertex in edge :
			glVertex3fv(mountain_vertices[vertex])
	glEnd()

def Road():
	glBegin(GL_LINES)
	for edge in road_edges:
		for vertex in edge :
			glVertex3fv(road_vertices[vertex])
	glEnd()


def Sun():
	posx = 0.75  
	posy = 0.75
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
	display = (600,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	pygame.display.set_caption("scenery of mountain","scenery")
	# gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	# glTranslatef(0.0,.0, -5)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Background()
		Sun()
		Mountain()
		Road()
		pygame.display.flip()
		pygame.time.wait(10)

main()