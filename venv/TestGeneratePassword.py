import unittest
import string
from generate_password import generate_password

class TestGeneratePassword(unittest.TestCase):
    def test_length(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)

    def test_num(self):
        password = generate_password(10, nums=3)
        self.assertGreaterEqual(sum(c.isdigit() for c in password), 3)

    def test_special_chars(self):
        password = generate_password(10, special_chars=2)
        self.assertGreaterEqual(sum(c in string.punctuation for c in password), 2)

    def test_uppercase(self):
        password = generate_password(10, uppercase=2)
        self.assertGreaterEqual(sum(c.isupper() for c in password), 2)

    def test_lowercase(self):
        password = generate_password(10, lowercase=2)
        self.assertGreaterEqual(sum(c.islower() for c in password), 2)

if __name__ == '__main__':
    unittest.main()