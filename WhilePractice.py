# Дан список чисел
# [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа
# до тех пор, пока не встретите отрицательное
# или не закончится список (выход за границу).

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index <= len(my_list):
    if my_list[index] > 0:
        print(my_list[index])
        index += 1
        continue

    elif my_list[index] == 0:
        index += 1
        continue

    else:
        break