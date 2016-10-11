from __future__ import division
from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext


class Vector(object):
    def __init__(self, coordinates):
        try:
            getcontext().prec = 10

            if not coordinates:
                raise ValueError
            # Make coordinates a Decimal for better precision
            # Use a list comprehension to convert each component to Decimal
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            # self.coordinates = tuple([x for x in coordinates])
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
        # result = [x * c for x in self.coordinates]

        return Vector(result)

    def get_magnitude(self):
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))
        # return sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalize(self):
        """Get the unit vector"""
        try:
            return self.scalar_multiply(Decimal('1.0')/self.get_magnitude())
            # return self.scalar_multiply(1.0 / self.get_magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector.')

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def get_theta(self, v, in_degrees=False):
        if self.is_zero() or v.is_zero():
            raise Exception('Cannot get the angle between the zero vector and another vector.')  # noqa

        if in_degrees:
            return degrees(
                acos(self.normalize().dot_product(v.normalize())))
        else:
            return acos(self.normalize().dot_product(v.normalize()))

    def is_parallel_to(self, v):
        if self.dimension != v.dimension:
            raise Exception('Vectors must have the same # of dimensions.')

        result = True
        multipliers = [y / x for x, y in zip(self.coordinates, v.coordinates)]

        for i in range(self.dimension - 1):
            if multipliers[i] != multipliers[i+1]:
                result = False
                break

        return result

    # def is_parallel_to(self, v):
    #     if self.dimension != v.dimension:
    #         raise Exception('Vectors must have the same # of dimensions.')
    #
    #     return (self.is_zero() or
    #             v.is_zero() or
    #             self.get_theta(v) == 0 or
    #             self.get_theta(v) == pi)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        """
        Determines if two vectors are orthogonal (their dot product is zero)
        """
        if self.dimension != v.dimension:
            raise Exception('Vectors must have the same # of dimensions.')

        return abs(self.dot_product(v)) < tolerance

    def is_zero(self, tolerance=1e-10):
        return self.get_magnitude() < tolerance

    def get_v_parallel(self, b):
        """
        Project the vector v onto a base vector b and
        get the component of v that is parallel to b
        :param b: base vector
        :return: vector v parallel (the component of v that is parallel to b)
        """
        return b.normalize().scalar_multiply(self.dot_product(b.normalize()))

    def get_v_perp(self, b):
        """
        Project the vector v onto a base vector b and
        get the component of v that is orthogonal to b
        :param b: base vector
        :return: vector v perp (the component of v that is orthogonal to b)
        """
        return self.subtract(self.get_v_parallel(b))
