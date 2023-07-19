from main import pairs
from unittest import TestCase

class TestPairs(TestCase):
    def test_of_list(self):
        list_1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
        list_2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
        expected = ['Alex и Emma', 'Arthur и Kate', 'John и Kira', 'Peter и Liza', 'Richard и Trisha']
        res = pairs(list_1, list_2)
        self.assertEqual(res, expected, "Lists aren`t equal")


