import unittest

from utils import power


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)


if __name__ == "__main__":
    unittest.main()