from __future__ import division
from vector import Vector
import unittest


class TestVectors(unittest.TestCase):
    def test_init(self):
        vector1 = Vector([7, 2, 6])

        self.assertEqual(vector1.coordinates, (7, 2, 6))
        self.assertEqual(vector1.dimension, 3)
        with self.assertRaises(ValueError):
            vector2 = Vector(None)
        with self.assertRaises(TypeError):
            vector3 = Vector(9)

    def test_eq(self):
        vector1 = Vector([1, 2, 3])
        vector2 = Vector([1, 2, 3])
        vector3 = Vector([4, 5, 6])

        self.assertTrue(vector1 == vector2)
        self.assertFalse(vector1 == vector3)

    def test_add(self):
        vector1 = Vector([8, -9])
        vector2 = Vector([-1, 2])

        self.assertEqual(vector1.add(vector2), Vector([7, -7]))

    def test_subtract(self):
        vector1 = Vector([8, -9])
        vector2 = Vector([-1, 2])

        self.assertEqual(vector1.subtract(vector2), Vector([9, -11]))

    def test_scalar_multiply(self):
        vector1 = Vector([9, -4, 7])

        self.assertEqual(vector1.scalar_multiply(3), Vector([27, -12, 21]))

    def test_get_magnitude(self):
        vector1 = Vector([1, -2, 3])
        self.assertEqual(round(vector1.get_magnitude(), 3), 3.742)

    def test_normalize(self):
        vector1 = Vector([2, 3])

        self.assertEqual(round(vector1.normalize().coordinates[0], 3),
                         0.555)
        self.assertEqual(round(vector1.normalize().coordinates[1], 3),
                         0.832)

    def test_dot_product(self):
        vector1 = Vector([-1, 2, 3])
        vector2 = Vector([4, -5, 6])

        self.assertEqual(vector1.dot_product(vector2), 4)

    def test_get_theta(self):
        vector1 = Vector([-1, 2, 3])
        vector2 = Vector([4, -5, 6])

        self.assertEqual(round(vector1.get_theta(vector2), 3),
                         1.449)
        self.assertEqual(round(vector1.get_theta(vector2, True), 3),
                         82.998)

    def test_is_parallel_to(self):
        vector1 = Vector([2, 3])
        vector2 = Vector([1, 1.5])
        vector3 = Vector([8, 9])
        vector4 = Vector([1, 2])
        vector5 = Vector([7, 1.5])
        zeroVector = Vector([0, 0])

        self.assertEqual(vector1.is_parallel_to(vector2), True)
        self.assertEqual(vector1.is_parallel_to(zeroVector), True)

        self.assertEqual(vector1.is_parallel_to(vector3), False)
        self.assertEqual(vector1.is_parallel_to(vector4), False)
        self.assertEqual(vector1.is_parallel_to(vector5), False)

        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        self.assertEqual(v.is_parallel_to(w), True)

        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        self.assertEqual(v.is_parallel_to(w), False)

        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])
        self.assertEqual(v.is_parallel_to(w), False)

        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        self.assertEqual(v.is_parallel_to(w), True)

    def test_is_orthogonal_to(self):
        vector1 = Vector([0, 3])
        vector2 = Vector([2, 0])
        vector3 = Vector([1, 1])
        zeroVector = Vector([0, 0])

        self.assertEqual(vector1.is_orthogonal_to(vector2), True)
        self.assertEqual(vector1.is_orthogonal_to(zeroVector), True)
        self.assertEqual(zeroVector.is_orthogonal_to(zeroVector), True)

        self.assertEqual(vector1.is_orthogonal_to(vector3), False)

        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        self.assertEqual(v.is_orthogonal_to(w), False)

        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        self.assertEqual(v.is_orthogonal_to(w), False)

        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])
        self.assertEqual(v.is_orthogonal_to(w), True)

        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        self.assertEqual(v.is_orthogonal_to(w), True)

    def test_z(self):
        print '\n'

# One way to run the tests from the comnad line
# if __name__ == '__main__':
#     unittest.main()

# Another way to run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestVectors)
unittest.TextTestRunner(verbosity=2).run(suite)
