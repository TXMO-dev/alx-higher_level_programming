import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_multiply_by_two(self):
        base = Base(5)
        result = base.multiply_by_two()
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
