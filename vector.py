from math import sqrt, acos, degrees
from decimal import Decimal


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            # Make coordinates a Decimal for better precision
            # Use a list comprehension to convert each component to Decimal
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty.')

        except TypeError:
            raise TypeError('The coordinates must be an iterable.')

    def __str__(self):
        # {} implicitly references the first positional argument
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        result = []

        # Using a for loop
        # if self.dimension == v.dimension:
        #     for i in range(self.dimension):
        #         result.append(self.coordinates[i] + v.coordinates[i])
        # else:
        #     raise ValueError('Vectors must have the same # of dimensions.')

        # Using a list comprehension
        if self.dimension == v.dimension:
            result = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        else:
            raise ValueError('Vectors must have the same # of dimensions.')

        return Vector(result)

    def subtract(self, v):
        result = []

        # Using a for loop
        # if self.dimension == v.dimension:
        #     for i in range(self.dimension):
        #         result.append(self.coordinates[i] - v.coordinates[i])
        # else:
        #     raise ValueError('Vectors must have the same # of dimensions.')

        # Using a list comprehension
        if self.dimension == v.dimension:
            result = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        else:
            raise ValueError('Vectors must have the same # of dimensions.')

        return Vector(result)

    def scalar_multiply(self, c):
        # Using a for loop
        # result = []
        # for i in range(self.dimension):
        #     result.append(self.coordinates[i] * c)

        # Using a list comprehension
        result = [x * Decimal(c) for x in self.coordinates]

        return Vector(result)

    def get_magnitude(self):
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))

    def normalize(self):
        try:
            return self.scalar_multiply(Decimal('1.0')/self.get_magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector.')

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def get_theta(self, v, in_degrees=False):
        if self.get_magnitude() == 0 or v.get_magnitude() == 0:
            raise Exception('Cannot get the angle between the zero vector and another vector.')  # noqa

        if in_degrees:
            return degrees(
                acos(self.normalize().dot_product(v.normalize())))
        else:
            return acos(self.normalize().dot_product(v.normalize()))
