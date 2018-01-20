# -*- coding: utf-8 -*-

from pyglet.gl import *
from vector import vector
from helpers import drawing

G = vector(0.0, 0.0, -9.8)

class Ball(object):
    
    def __init__(self, color, mass, radius, pos, velocity):
        self.__Color    = color
        self.__Mass     = float(mass)
        self.__Radius   = float(radius)
        self.__Pos      = vector(pos)
        self.__Velocity = vector(velocity)
        
    @property
    def color(self):
        return self.__Color
    
    @property
    def mass(self):
        return self.__Mass
    
    @property
    def radius(self):
        return self.__Radius
    
    @property
    def pos(self):
        return self.__Pos
    
    @property
    def vel(self):
        return self.__Velocity
    
    def move(self, dt):
        if (self.pos.z - self.radius) < -2.0:
            if self.vel.z < 0:
                self.vel.z = - self.vel.z
        self.__Pos += self.__Velocity*dt + G*dt*dt*0.5
        self.__Velocity += G*dt
        
    
    def draw(self):
        with drawing():
            glTranslatef(*self.pos)
            Q = gluNewQuadric()
            try:
                glColor3f(*self.color)
                gluSphere( Q, self.radius, 30, 30)
            finally:
                gluDeleteQuadric(Q)
        
       
    
    
        