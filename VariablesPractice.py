#1st
completed_homework = 12 #Завершённые Д/З

#2nd
hours_spent = 1.5 #Затраченные часы

#3rd
course_name = "Python" #Название курса

#4th
average = hours_spent / completed_homework #Среднее арифметическое время на одно Д/З

#Вывод №1 Через % форматирование, вроде как так называется ( ͠° ͟ʖ ͡°)
print("Курс: %s," % course_name,
      "всего задач:%s," % completed_homework,
      "затрачено часов: %s," % hours_spent,
      "среднее время выполнения %s" % average, "часа.\n")

#Вывод №2 Через любимую конкатенацию
print("Курс: " +  course_name + \
       ", всего задач:" + str(completed_homework) + \
       ", затрачено часов: " + str(hours_spent) + \
       ", среднее время выполнения " + str(average) + " часа.\n")

#Вывод №3 Через f-string
print(f'Курс: {course_name}, '
      f'всего задач:{completed_homework}, '
      f'затрачено часов: {hours_spent}, '
      f'среднее время выполнения {average} часа.')

""" Поигрался с форматированием для себя,
    чтобы понять что ближе по использованию, ибо конкатенация - отстой.
    Общий вывод: всё же удобнее через f-string :-) """