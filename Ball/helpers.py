#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager 
from pyglet.gl import *

__all__ = ('Figure', 'drawing')

class Figure(object):
    
    def __init__(self, kind):
        self.__Kind = kind
        
    def __enter__(self): # pri vhode v kontekst
        glBegin(self.__Kind)
        return self
        
        
    def __exit__(self, exc_type, exc_value, traceback):
        glEnd()
        return False
    
@contextmanager    
def drawing():
    glPushMatrix()
    try:
        yield
    finally:
        glPopMatrix