# -*- coding: utf-8 -*-

class _coords_iterator(object):
    
    def __init__(self, coords):
        self.__Coords = list(coords)
        
    def __next__(self):
        if len(self.__Coords) <= 0:
            raise StopIteration()
        R = self.__Coords[0]
        del self.__Coords[0]
        return R



class vector(object):
    
    def __new__(cls, x,y=None, z=None):
        if isinstance(x, vector):
            return x
        else:
            #return object.__new__(cls)
            return super(cls,cls).__new__(cls)
    
    @property
    def z(self):
        return self.__Data[2]
    
    @z.setter
    def z(self, value):
        self.__Data[2]=float(value)
    
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
                if isinstance(x, str):
                    raise TypeError()
                x, y, z = map(float,x)
            except TypeError:
                x, y, z = map(float, (x,y,z,))
            self.__Data = list((x,y,z,))
    
    def __iter__(self):
        return _coords_iterator(self.__Data)
    
    def __str__(self):
            return '<{0:+8.3f},{1:+8.3f},{2:+8.3f}>'.format(*self.__Data)
##        return '{},{},{}'.format(*self.__Data)
        
    __repr__=__str__
        
    def __add__(self, other):
        x1, y1, z1 = self.__Data
        x2, y2, z2 = other.__Data
        return vector (x1+x2, y1+y2, z1+z2)
        
    def __mul__ (self, number):
        x1, y1, z1 = self.__Data
        return vector (number*x1, number*y1, number*z1)
        
    __rmul__ = __mul__
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        