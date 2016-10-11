from __future__ import division
from vector import Vector
from decimal import Decimal
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
                         83.002)

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

    def test_get_v_parallel(self):
        v = Vector([3.039, 1.879])
        b = Vector([0.825, 2.036])
        self.assertEqual(v.get_v_parallel(b),
                         Vector((Decimal('1.082606963'),
                                 Decimal('2.671742759'))))

        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        self.assertEqual(v.get_v_parallel(b),
                         Vector([Decimal('1.968516167'),
                                 Decimal('-2.810760749'),
                                 Decimal('0.8480849635'),
                                 Decimal('2.679813233')]))

    def test_get_v_perp(self):
        v = Vector([-9.88, -3.264, -8.159])
        b = Vector([-2.155, -9.353, -9.473])
        self.assertEqual(v.get_v_perp(b),
                         Vector([Decimal('-8.350081043'),
                                 Decimal('3.376061254'),
                                 Decimal('-1.433746042')]))

        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        self.assertEqual(v.get_v_perp(b),
                         Vector([Decimal('1.040483833'),
                                 Decimal('-3.361239251'),
                                 Decimal('2.843915037'),
                                 Decimal('-5.189813233')]))

    def test_z(self):
        print '\n'

# One way to run the tests from the comnad line
# if __name__ == '__main__':
#     unittest.main()

# Another way to run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestVectors)
unittest.TextTestRunner(verbosity=2).run(suite)
