import unittest
from main import *

one_to_many = create_1m()
many_to_many = create_mm()

class TestMain(unittest.TestCase):
    def test_A1(self):
        self.assertEqual(solve_a1(one_to_many),
                         [('Java', 'Java SE 21', 17.18, 'Eclipse', 2022), ('C++', 'C++20', 6.49, 'IntelliJ IDEA', 2023),
                          ('GO', '1.21.3', 36.1, 'Komodo', 2022), ('C#', '11', 6.94, 'Microsoft Visual Studio', 2023),
                          ('Python', '3.11', 29.48, 'Visual Studio Code', 2023),
                          ('C', 'C17', 6.49, 'Visual Studio Code', 2023)])

    def test_A2(self):
        self.assertEqual(solve_a2(one_to_many), [('Komodo', 36.1), ('Visual Studio Code', 35.97), ('Eclipse', 17.18),
                                                 ('Microsoft Visual Studio', 6.94), ('IntelliJ IDEA', 6.49)])

    def test_A3(self):
        self.assertEqual(solve_a3(many_to_many), {'Microsoft Visual Studio': ['C#', 'Python', 'C++'],
                                      'Visual Studio Code': ['Python', 'C', 'C#', 'C++']})


if __name__ == "__main__":
    unittest.main()
