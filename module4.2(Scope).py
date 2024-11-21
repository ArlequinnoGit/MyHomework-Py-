def test_function(): # Родительская функция
    def inner_function(): # Дочерняя функция
        a = "Я в области видимости функции test_function"
        print(a)
    return inner_function()

test_function()
#inner_function() - Без комента выдаёт ошибку,
                  # Ибо функция находится в непосредственной области видимости ;)
"""
NameError: name 'inner_function' is not defined.
Did you mean: 'test_function'?
"""

