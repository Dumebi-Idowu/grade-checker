import unittest
from grade_checker import get_grade

class TestGradeChecker(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(get_grade(75), 'A')
        self.assertEqual(get_grade(70), 'A')

    def test_grade_b(self):
        self.assertEqual(get_grade(65), 'B')
        self.assertEqual(get_grade(60), 'B')

    def test_grade_c(self):
        self.assertEqual(get_grade(55), 'C')
        self.assertEqual(get_grade(50), 'C')

    def test_grade_d(self):
        self.assertEqual(get_grade(47), 'D')
        self.assertEqual(get_grade(45), 'D')

    def test_grade_f(self):
        self.assertEqual(get_grade(44), 'F')
        self.assertEqual(get_grade(0),  'F')

if __name__ == "__main__":
    unittest.main()