#Countdown from 5
for countdown in (5,4,3,2,1,"Hey"):
    print(countdown)
for countdown in range (5,-1,-1):
    print(countdown)

#Emulating Numeric Types
from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self): # How the objects are represented
        return 'Vector(%r,%r)' % (self.x, self.y)
    def __abs__(self): # Gives the magnitude of each vectors
        return hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other): # allows objects to be added
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.x
        return Vector(x,y)
    def __mul__(self, scalar):# allows object to be multiplied by num
        return Vector(self.x * scalar, self.y * scalar)
    def __getitem__(self, item): # Makes object to support indexing
        return self.x if item == 0 else self.y

if __name__ == '__main__':
    v1 = Vector(2,1)
    v2 = Vector(2,4)
    v3 = v1 + v2

    import matplotlib.pyplot as plt
    ax = plt.axes()
    ax.arrow(0,0, v1[0]/6,v1[1]/6, head_width=0.05, head_length=0.1, label=v1.__repr__(),fc='k', ec='k')
    ax.arrow(0, 0, v2[0]/6, v2[1]/6, head_width=0.05, head_length=0.1,label=v2.__repr__(),fc='k', ec='k')
    ax.arrow(0, 0, v3[0]/6, v3[1]/6, head_width=0.05, head_length=0.1,label=v3.__repr__(), fc='k', ec='k')
    plt.show()