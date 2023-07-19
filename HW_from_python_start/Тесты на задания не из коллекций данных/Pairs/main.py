boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


def pairs(list_1: list[str], list_2: list[str]) -> list[str]:
    print('Идеальные пары:')
    perfect_pairs = []
    list_1.sort()
    list_2.sort()
    for boy_name, girl_name in zip(list_1, list_2):
        pair = f'{boy_name} и {girl_name}'
        perfect_pairs.append(pair)

    return perfect_pairs

print(pairs(boys, girls))