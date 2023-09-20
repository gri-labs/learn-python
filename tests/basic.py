import unittest


class BasicTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)


# run tests
if __name__ == '__main__':
    unittest.main()
