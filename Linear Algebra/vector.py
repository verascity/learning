class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        multi_coords = [c*x for x in self.coordinates]
        return Vector(multi_coords)


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
