# 1 Создайте переменную my_dict
# и присвойте ей словарь из нескольких пар ключ-значение.
my_dict = {'Common' : 1, 'Uncommon' : 2, 'Rare' : 3,
           'UltraRare' : 4, 'Epic' : 5}

# Выведите на экран словарь my_dict.
print(my_dict)

# Выведите на экран одно значение по существующему ключу;
print(my_dict['Common'])
# Одно по отсутствующему из словаря my_dict без ошибки.
my_dict ['Mythical'] = 6
print(my_dict['Mythical'])


#Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Mythical': 6, 'Legendary': 7})

# Удалите одну из пар в словаре по существующему ключу из словаря my_dict
# и выведите значение из этой пары на экран.
print(my_dict.pop('Common'))
print(my_dict)

# 2 Работа со множествами:
# Создайте переменную my_set и присвойте ей множество,
# состоящее из разных типов данных с повторяющимися значениями.
my_set = {'StringText', 412, False, True,
          True, 'Homework', 'StringText', 412}

# Выведите на экран множество my_set
# (должны отобразиться только уникальные значения).
print(my_set)

#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#Можно добавлять по одному:
my_set.add('Aboba')
my_set.add('Python')

# Удалите один любой элемент из множества my_set.
# Через .discard или
# Через .remove (my_set.remove('Aboba'))
my_set.discard('Aboba')

# Выведите на экран измененное множество my_set.
print(my_set)

