import unittest
from models.other_module import OtherModule


class TestOtherModule(unittest.TestCase):
    def test_get_name(self):
        other_module = OtherModule("Alice")
        result = other_module.get_name()
        self.assertEqual(result, "Alice")


if __name__ == '__main__':
    unittest.main()
