# -*- coding: utf-8 -*-

class vector(object):
    
    def __new__(cls, x,y=None, z=None):
        if isinstance(x, vextor):
            return x
        else:
            return object.__new__(cls)
        #return super(cls,cls).__new__(cls)
    
    def __init__(self,x,y=None, z=None):
        '''
        Вектор может быть задан:
        тремя координатами,
        другим вектором,
        последовательностью из трех координат
        '''
        if isinstance(x,vector):
            pass
        else:
            try:
                x, y, z = map(float, x)
            except TypeError:
                x, y, z = map(float, (x,y,z))
            self.__Data = (x,y,z)
            
        def __str__(self):
##            return '{0:+8.3f}, {1:+8.3f}, {2:+8.3f}'.format(*self.__Data)
            return '{}, {}, {}'.format(*self.__Data)
        def __add__(self, other):
            x1, y1, z1 = self.__Data
            x2, y2, z2 = Other.__Data
            return vector (x1+x2, y1+y2, z1+z2)
        
        def __mul__ (self, number):
            x1, y1, z1 = self.__Data
            return vector (number*x1, number*y1, number*z1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        