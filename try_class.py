# -*- coding: utf-8 -*-

class Ball(object):
    """
    Класс описывающий свойства шариков
    """
    
    def __init__(self, radius, color, massa, speed):
        self.radius = radius
        self.color = color
        self.massa = massa
        self.speed = speed 
    
    @property    
    def diametr(self):
        x = self.radius * 2
        return x
    
    @property
    def impuls(self):
        impuls = self.massa * self.speed
        return impuls
    
    def blow(self):
        return "Шарик с массой '{}' взорвался нахуй".format(self.massa)
    
    def __str__(self):
        return 'радиус={}, цвет={}, масса={}, скорость={}, диаметр={}, импульс={}'.format(self.radius,
                                                                                          self.color,
                                                                                          self.massa,
                                                                                          self.speed,
                                                                                          self.diametr,
                                                                                          self.impuls)
                                                                                       
    
def sravnit_impuls(b1,b2):
    if b1.impuls > b2.impuls:
        return b2.blow()
    elif b1.impuls < b2.impuls:
        return b1.blow()
    else:
        return 'Никто не взорвался, одинковый импульс'
    
        
if __name__ == '__main__':
    ball1 = Ball(radius=25, color='red', massa=78, speed=105)
    ball2 = Ball(radius=43, color='green', massa=9999, speed=0.1)
    print(sravnit_impuls(ball1,ball2))
    

    