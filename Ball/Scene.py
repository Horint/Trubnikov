#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
from pyglet import clock
from helpers import Figure
from Ball import Ball


class Scene(pyglet.window.Window):
    
    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION,
            (gl.c_float*4)(5.0, 5.0, 5.0, 1.0))
        self.__B1 = Ball(color=(1.0, 0.0, 0.0), mass=1.0, radius=0.1,
                                pos=(0,-1.0,2.0), velocity=(0.0, 0.003, 0.0))
        clock.schedule_interval(self.on_clock_tick, 1/30)
        
        
    def on_resize(self, width, height):
        glViewport (0,0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, width/height, 0.1, 1000.0)
        gluLookAt (5.0, 0.0, 0.0,
                   0.0, 0.0, 0.0,
                   0.0, 0.0, 1.0                )
                
        glMatrixMode(GL_MODELVIEW) 
        glLoadIdentity()
##        glScalef(height/width, 1.0, 1.0)
##        glScalef(10.0, 10.0, 10.0)
    
    def on_clock_tick(self, dt):
        N = 100
        for k in range (0, N):
            self.__B1.move(dt/N)
    
    def on_draw(self):
        self.clear()
        self.__B1.draw()
        glColor3f(1.0, 1.0, 1.0)
        with Figure(GL_TRIANGLES):
            glVertex3f(-5.0,-5.0, -2.0)
            glVertex3f(-5.0, 5.0, -2.0)
            glVertex3f( 5.0, 5.0, -2.0)
            glVertex3f(-5.0,-5.0, -2.0)
            glVertex3f( 5.0,-5.0, -2.0)
            glVertex3f( 5.0, 5.0, -2.0)

        