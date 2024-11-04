def print_params(a=1, b='строка', c=True):
    print(f'a={a}, b={b}, c={c}')

# Часть 1: Вызов функции с разными аргументами
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Часть 2: Распаковка параметров
values_list = [10, 'другая строка', False]
values_dict = {'a': 100, 'b': 'словарь', 'c': None}

print_params(*values_list)
print_params(**values_dict)

# Часть 3: Распаковка + отдельные параметры
values_list_2 = ['ещё одна строка', 50]

print_params(*values_list_2, c=42)