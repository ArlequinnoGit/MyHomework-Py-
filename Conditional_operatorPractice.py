# На вход программе подаются 3 целых числа
# и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию
# (из if, elif, else), которая выводит кол-во
# одинаковых чисел среди 3-х введённых

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))

#ЕСЛИ 1 число = 2 число = 3 число:
if first_num == second_num == third_num:
    print("3")

#ЕСЛИ 1 число = 2 число ИЛИ
#     2 число = 3 число ИЛИ
#     1 число = 3 число:
elif first_num == second_num or \
    second_num ==  third_num or \
    first_num == third_num:
    print("2")

#ИНАЧЕ:
else:
    print("0")