def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка наличия '@' в адресе
    if '@' not in sender or '@' not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверяем, что отправитель и получатель не совпадают
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверяем, является ли отправителем университетская почта
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Примеры использования функции
send_email("Hello!", "student@example.com")  # Использует стандартного отправителя
send_email("Hi there!", "student@example.com", sender="professor@university.edu")  # Нестандартный отправитель
send_email("Test message", "invalid-email")  # Некорректный email получателя
send_email("Self test", "university.help@gmail.com")  # Отправка самому себе
send_email("Another test", "student@example.com", sender="university.help@gmail.com")  # Стандартная отправка
