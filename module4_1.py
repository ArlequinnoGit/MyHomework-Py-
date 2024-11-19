from true_math import divide as true
from fake_math import  divide as fake

true1res = true(5, 1) # Должно выйти 5, ибо 5 / 1 = 5
true2res = true(5, 0) # Бесконечность, ибо высшая математика

fake1res = fake(10, 1) # Должно выйти 10, ибо 10 / 1  = 10
fake2res = fake(10, 0) # Ошибка, ибо на ноль делить нельзя!!