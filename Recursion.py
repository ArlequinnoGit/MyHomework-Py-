def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства работы с отдельными цифрами
    str_number = str(number)

    if len(str_number) == 1:
        # Если осталось одно число, проверяем, не является ли оно нулём
        digit = int(str_number)
        return digit if digit != 0 else 1

    # Берем первую цифру числа
    first = int(str_number[0])

    if first == 0:
        # Пропускаем нуль и продолжаем обработку оставшихся цифр
        return get_multiplied_digits(int(str_number[1:]))
    else:
        # Рекурсивный вызов функции для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(402030))
