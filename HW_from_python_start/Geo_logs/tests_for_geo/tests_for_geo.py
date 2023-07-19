from unittest import TestCase
from main import filter_country, geo_logs
import pytest

class TestFilterCountry(TestCase):
    def test_filter_country_with_Russia(self):
        list_1 = geo_logs
        country = 'Россия'
        expected = [{'visit1': ['Москва', 'Россия']},
 {'visit3': ['Владимир', 'Россия']},
 {'visit7': ['Тула', 'Россия']},
 {'visit8': ['Тула', 'Россия']},
 {'visit9': ['Курск', 'Россия']},
 {'visit10': ['Архангельск', 'Россия']}]
        res = filter_country(list_1, country)
        self.assertEqual(res, expected, "Country is not in list")

@pytest.mark.parametrize(
    "list_1, country, expected", [
        (geo_logs, 'Индия', [{'visit2': ['Дели', 'Индия']}]),
        (geo_logs, 'Франция', [{'visit5': ['Париж', 'Франция']}]),
        (geo_logs, 'Португалия',[{'visit4': ['Лиссабон', 'Португалия']}, {'visit6': ['Лиссабон', 'Португалия']}])
    ]
)
def test_filt_geo(list_1, country, expected):
    res = filter_country(list_1, country)
    assert res == expected




