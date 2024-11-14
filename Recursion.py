def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1
    if len(str_number) > 1:
        # Первая цифра
        first = int(str_number[0])
        # Остальные цифры
        remaining_digits = int(str_number[1:])
        # Возвращаем произведение первой цифры и оставшихся
        return first * get_multiplied_digits(remaining_digits)

    # Если длина строки равна 1
    elif len(str_number) == 1:
        # Возвращаем первую цифру
        return int(str_number)

print(get_multiplied_digits(40203))