calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Примеры вызовов функций
result_1 = string_info("Example")
result_2 = is_contains("Python", ["Java", "C++", "Python"])
result_3 = is_contains("ruby", ["RUBY", "Javascript", "PHP"])

# Вывод результатов
print(result_1)  # (7, 'EXAMPLE', 'example')
print(result_2)  # True
print(result_3)  # True

# Вывод общего числа вызовов
print(calls)  # 3