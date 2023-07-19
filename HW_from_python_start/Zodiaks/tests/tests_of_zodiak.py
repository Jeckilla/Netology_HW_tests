from unittest import TestCase
from main import zodiak
import pytest

class TestZodiak(TestCase):
    def test_zodiak_Kozerog(self):
        month = 'январь'
        day = 20
        expected = 'Знак зодиака: Козерог'
        res = zodiak(month, day)
        self.assertEqual(res, expected, "Result not equal expected 'Знак зодиака: Козерог'")


@pytest.mark.parametrize(
    "month, day, expected", [
        ('март', 6, 'Знак зодиака: Рыбы'),
        ('май', 25, 'Знак зодиака: Близнецы'),
        ('июль', 30, 'Знак зодиака: Лев'),
        ('август', 29, 'Знак зодиака: Дева'),
        ('октябрь', 25, 'Знак зодиака: Скорпион')
    ]
)
def test_zodiak_with_params(month, day, expected):
    res = zodiak(month, day)
    assert res == expected
