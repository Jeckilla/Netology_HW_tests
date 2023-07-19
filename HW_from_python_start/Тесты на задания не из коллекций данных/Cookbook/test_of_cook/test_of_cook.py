from unittest import TestCase
from main import shopping_list, cook_book


class TestShoppingList(TestCase):
    def test_of_shopping_dict(self):
        person = 5
        list = cook_book
        expected = {'Пицца': ['сыр, 250 гр.',
           'томаты, 250 гр.',
           'тесто, 500 гр.',
           'бекон, 150 гр.',
           'колбаса, 150 гр.',
           'грибы, 100 гр.'],
 'Салат': ['картофель, 500 гр.',
           'морковь, 250 гр.',
           'огурцы, 250 гр.',
           'горошек, 150 гр.',
           'майонез, 350 гр.'],
 'Суп': ['картофель, 1000 гр.',
         'морковь, 500 гр.',
         'мясо, 500 гр.',
         'лук, 250 гр.',
         'зелень, 250 гр.'],
 'Фруктовый десерт': ['хурма, 300 гр.',
                      'киви, 300 гр.',
                      'творог, 300 гр.',
                      'сахар, 50 гр.',
                      'мед, 250 гр.']}
        res = shopping_list(person, list)
        self.assertEqual(res, expected)