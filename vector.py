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
        result = [x * c for x in self.coordinates]

        return Vector(result)
