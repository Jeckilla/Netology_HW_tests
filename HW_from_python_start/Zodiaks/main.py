def zodiak(month, day):
    if (month == 'декабрь' and day >= 22) or (month == 'январь' and day <= 20):
        return 'Знак зодиака: Козерог'
    elif (month == 'январь' and day >= 21) or (month == 'февраль' and day <= 19):
        return 'Знак зодиака: Водолей'
    elif (month == 'февраль' and day >= 20) or (month == 'март' and day <= 20):
        return 'Знак зодиака: Рыбы'
    elif (month == 'март' and day >= 21) or (month == 'апрель' and day <= 20):
        return 'Знак зодиака: Овен'
    elif (month == 'апрель' and day >= 21) or (month == 'май' and day <= 21):
        return 'Знак зодиака: Телец'
    elif (month == 'май' and day >= 22) or (month == 'июнь' and day <= 21):
        return 'Знак зодиака: Близнецы'
    elif (month == 'июнь' and day >= 22) or (month == 'июль' and day <= 22):
        return 'Знак зодиака: Рак'
    elif (month == 'июль' and day >= 23) or (month == 'август' and day <= 21):
        return 'Знак зодиака: Лев'
    elif (month == 'август' and day >= 22) or (month == 'сентябрь' and day <= 23):
        return 'Знак зодиака: Дева'
    elif (month == 'сентябрь' and day >= 24) or (month == 'октябрь' and day <= 23):
        return 'Знак зодиака: Весы'
    elif (month == 'октябрь' and day >= 24) or (month == 'ноябрь' and day <= 22):
        return 'Знак зодиака: Скорпион'
    elif (month == 'ноябрь' and day >= 23) or (month == 'декабрь' and day <= 22):
        return 'Знак зодиака: Стрелец'
    else:
        return 'Неверное название месяца или число.'


result = zodiak('январь', 20)
print(result)
