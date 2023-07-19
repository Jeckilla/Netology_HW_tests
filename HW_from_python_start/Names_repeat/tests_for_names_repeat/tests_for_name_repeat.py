import pytest
from unittest import TestCase
from main import count_repeat, mentors

class TestNamesRepeat(TestCase):
    def test_equal_expected_and_res(self):
        list = mentors
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        res = count_repeat(list)
        self.assertEqual(res, expected, "Values in string is incorrect")

def test_of_names_repeat():
    list = mentors
    expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    res = count_repeat(list)
    assert res == expected
