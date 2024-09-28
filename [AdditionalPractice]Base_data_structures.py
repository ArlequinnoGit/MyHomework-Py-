# СРЕДНИЙ БАЛЛ

# Оценки учеников
grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]

# Студенты
students = {'Jonny', 'Bilbo',
            'Steve', 'Khendrik',
            'Aaron'}

# Оценки распределяются по алфавитному порядку соответственно:
# Aaron, Bilbo, Jonny, Khendrik, Steve.

# Перевожу множество students в список, затем использую метод sorted(),
# чтобы отсортировать имена студентов в алфавитном порядке.

# Я не помню, изучали ли мы этот метод (сам загуглил, каюсь),
# ибо если просто переводить множество в список - он не сортируется,
# а выдаёт рандомные значения из списка.
average_grades = \
    {sorted(list(students))[0]: sum(grades[0]) / len(grades[0]),
     sorted(list(students))[1]: sum(grades[1]) / len(grades[1]),
     sorted(list(students))[2]: sum(grades[2]) / len(grades[2]),
     sorted(list(students))[3]: sum(grades[3]) / len(grades[3]),
     sorted(list(students))[4]: sum(grades[4]) / len(grades[4])}

print(average_grades)