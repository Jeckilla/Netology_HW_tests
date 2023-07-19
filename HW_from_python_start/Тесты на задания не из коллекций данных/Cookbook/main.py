from pprint import pprint

cook_book = [
    ['салат',
     [
         ['картофель', 100, 'гр.'],
         ['морковь', 50, 'гр.'],
         ['огурцы', 50, 'гр.'],
         ['горошек', 30, 'гр.'],
         ['майонез', 70, 'мл.'],
     ]
     ],
    ['пицца',
     [
         ['сыр', 50, 'гр.'],
         ['томаты', 50, 'гр.'],
         ['тесто', 100, 'гр.'],
         ['бекон', 30, 'гр.'],
         ['колбаса', 30, 'гр.'],
         ['грибы', 20, 'гр.'],
     ],
     ],
    ['фруктовый десерт',
     [
         ['хурма', 60, 'гр.'],
         ['киви', 60, 'гр.'],
         ['творог', 60, 'гр.'],
         ['сахар', 10, 'гр.'],
         ['мед', 50, 'мл.'],
     ]
     ],
    ['суп',
     [
         ['картофель', 200, 'гр.'],
         ['морковь', 100, 'гр.'],
         ['мясо', 100, 'гр.'],
         ['лук', 50, 'гр.'],
         ['зелень', 50, 'гр.'],
     ]
     ]
]


def shopping_list(person: int, list: list[list[list[list]]]):
    shopping_list_final = {}
    for recip, products in list:
        key = f'{recip.capitalize()}'
        list_of_ingredients = []
        for prod, gramm, gr in products:
            gramm *= person
            product = f'{prod}, {gramm} гр.'
            list_of_ingredients.append(product)
            shopping_list_final[key] = list_of_ingredients
    return shopping_list_final

pprint(shopping_list(5, cook_book))
