def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру для сравнения без учета регистра
    root_word = root_word.lower()

    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Перебираем каждое слово из переданной последовательности
    for word in other_words:
        # Приводим текущее слово к нижнему регистру для сравнения без учета регистра
        if root_word in word.lower():
            # Если корневое слово содержится в текущем слове, добавляем его в результат
            same_words.append(word)

    # Возвращаем найденные однокоренные слова
    return same_words

# Вызываем функцию и выводим результат
result = single_root_words("able", "disablement", "ABLE", "abler", "disabled")
print(result)