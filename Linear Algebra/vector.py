from math import sqrt, acos, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
            
    def plus(self, v):
        added_coords = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(added_coords)
    
    def minus(self, v):
        sub_coords = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(sub_coords)
    
    def scalar_mult(self, c):
        multi_coords = [Decimal(c)*x for x in self.coordinates]
        return Vector(multi_coords)
    
    def magnitude(self):
        sqr_coords = [x**2 for x in self.coordinates]
        return Decimal(sqrt(sum(sqr_coords)))
    
    def normalize(self):
        try:
            unit_div = Decimal('1.0') / self.magnitude()
            return self.scalar_mult(unit_div)
        
        except ZeroDivisionError:
            raise Exception("Unable to normalize the zero vector!")
            
    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    def theta(self, v):
        rad_deg = input("In radians or degrees? Type r or d: ")
        
        num = self.dot_product(v)
        denom = self.magnitude() * v.magnitude()
        
        if denom == 0:
            raise Exception("Unable to return theta!")
        else:       
            
            if rad_deg == "r":
                return acos(num/denom)
            elif rad_deg == "d":
                return degrees(acos(num/denom))

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
