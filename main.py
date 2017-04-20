import pygame
from pygame.locals import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from math import *
import random

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

mountain1_vertices = (
    (-1.5,-1,0),
    (-0.5,0.25,0),
    (0.5,-1,0)
)


mountain2_vertices = (
    (-0.25,-1,0),
    (0.75,0.25,0),
    (1.75,-1,0)
)

mountain_edges = (
    (0,1),
    (1,2),
    (2,0)
)

mountain_colors = (
    (0.2,0.5,0.1),
    (0.8,0.8,0.8),
    (0.2,0.5,0.1),
    )

mountain_surfaces = (
    (0,1,2)
)

background_surfaces = (
    (0,1,2,3)
)
background_colors = (
    (0.8,0.9,1),
    (0,0.34,0.7),
    (0.2,0.44,0.7),
    (0.4,0.69,1)
    )
    
rainbow_colors = (
    (1,0,0,1),
    (1,0.6,0,1),
    (1,1,0,1),
    (0,1,0,1),
    (0,1,1,1),
    (0,0,1,1),
    (1,0,1,1)
)

def Background():
    glBegin(GL_QUADS)
    x = 0
    for vertex in background_surfaces:
        glColor3fv(background_colors[x])
        glVertex3fv(background_vertices[vertex])
        x += 1
    glEnd()

def Mountain():
    glBegin(GL_TRIANGLES)
    x = 0
    for vertex in mountain_surfaces:
        glColor3fv(mountain_colors[x])
        glVertex3fv(mountain2_vertices[vertex])
        x += 1
    
    y = 0
    for vertex in mountain_surfaces:
        glColor3fv(mountain_colors[y])
        glVertex3fv(mountain1_vertices[vertex])
        y += 1
    glEnd()
    
def rainbow(posX, posY):
    for x in range(7, 0, -1):
        HalfCircle(posX, posY, 0.1*x, rainbow_colors[7-x]);


def Sun():
    posx = 0.75  
    posy = 0.75
    posz = 0   
    sides = 32
    radius = 0.15
    glBegin(GL_POLYGON)
    x = 1;
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides) + posx    
        sine = radius * sin(i*2*pi/sides) + posy        
        glColor3fv((1,1,0.4))
        glVertex3f(cosine,sine, posz)
    glEnd()

def Circle(x, y, s, r):
    posx = x  
    posy = y
    posz = 0   
    sides = s
    radius = r
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i*2*pi/sides) + posx    
        sine = radius * sin(i*2*pi/sides) + posy        
        glColor3fv((1,1,1))
        glVertex3f(cosine,sine, posz)
    glEnd() 
    
def TriangleFan():
	x = 0
	y = 0
	radius = 0.2
	triangleAmount = 20
	glBegin(GL_TRIANGLE_FAN)
	glColor3fv((1,1,1))
	glVertex2f(x, y)
	
	for i in range(triangleAmount):
		glColor3fv((0,0,1))
		glVertex2f(x + (radius * cos(i *  pi / triangleAmount)), y + (radius * sin(i * pi / triangleAmount)))
		
	glEnd()
    
def LineLoop():
	lineAmount = 100
	x = 0
	y = 0
	radius = 0.2
	glBegin(GL_LINE_LOOP)
	for i in range(lineAmount):
		glColor3fv((0,0,1))
		glVertex2f(x + (radius * cos(i *  pi / lineAmount)), y + (radius* sin(i * pi / lineAmount)))

	glEnd() 


def HalfCircle(posX, posY, radius, color):
	posz = 0   
	sides = 100
	# radius = 0.15
	glBegin(GL_POLYGON)
	x = 1;
	
	#glColor3fv((1,1,1))
	#glVertex2f(posX, posY)
	
	glColor3fv((color[0]+0.7,color[1]+0.7,color[2]+0.7))	    
	glVertex2f(posX, posY+radius-0.15)    	
	for i in range(sides):
		cosine = radius * cos(i*pi/sides) + posX   
		sine = radius * sin(i*pi/sides) + posY  
		glColor4fv(color)	
		glVertex3f(cosine,sine, posz)
	

	glEnd() 
    
def Cloud(x, y):
    Circle(x,y,32,0.05)
    Circle(x,y+0.05,32,0.05)
    Circle(x-0.05,y-0.05,32,0.05)
    Circle(x-0.05,y+0.05,32,0.05)
    Circle(x-0.05,y+0.1,32,0.05)
    Circle(x-0.1,y-0.05,32,0.05)
    Circle(x-0.1,y,32,0.05)
    Circle(x-0.1,y+0.05,32,0.05)    
    Circle(x-0.15,y-0.05,32,0.05)
    Circle(x-0.15,y,32,0.05)
    Circle(x-0.15,y+0.05,32,0.05)
    Circle(x-0.15,y+0.1,32,0.05)
    Circle(x-0.2,y,32,0.05)
    Circle(x-0.2,y+0.05,32,0.05)

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
        rainbow(0.1,-0.52)
        Sun()
        Mountain()
        Cloud(-0.1, 0.6)
        Cloud(-0.5, 0.8)
        pygame.display.flip()
        pygame.time.wait(10)

main()
