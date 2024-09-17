#1st - Создайте переменную immutable_var
# и присвойте ей кортеж из нескольких элементов разных типов данных.

immutable_var = "string", True, 215, 1.5
print(immutable_var)

#2nd - Попытайтесь изменить элементы кортежа immutable_var.
# Объясните, почему нельзя изменить значения элементов кортежа.

#Python ругается на нас, ибо кортежи - неизменяемый тип данных.
#Мы не может заменять в нём элементы, однако есть исключения:
#Кортежи поддерживают конкатенацию и умножение на число.
#Чтобы программа работала дальше закомментировал строку ниже:

#immutable_var[0] = "not_string"

#3rd - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# Измените элементы списка mutable_list.
# Выведите на экран измененный список mutable_list.

#UNMODIFIED
mutable_list =  ["string", True, 215, 1.5]
print(mutable_list)

#MODIFIED
mutable_list[0] = "not_string"
mutable_list[1] = False
mutable_list[2] = 512
mutable_list[3] = 5.1
print(mutable_list)