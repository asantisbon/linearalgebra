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

        vector2 = Vector([-0.221, 7.437])
        vector3 = Vector([8.813, -1.331, -6.247])

    def test_get_unit_vector(self):
        vector1 = Vector([2, 3])

        self.assertEqual(round(vector1.get_unit_vector().coordinates[0], 3),
                         0.555)
        self.assertEqual(round(vector1.get_unit_vector().coordinates[1], 3),
                         0.832)


# One way to run the tests from the comnad line
# if __name__ == '__main__':
#     unittest.main()

# Another way to run the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestVectors)
unittest.TextTestRunner(verbosity=2).run(suite)
