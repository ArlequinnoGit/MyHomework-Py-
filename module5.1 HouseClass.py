class House: #Создаём класс House
    def __init__(self, name, numbers_of_floor): #Создаём метод __init__, в параметрах указатель self, метода имя и кол-во этажей
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor): #Создаём метод go_to, в параметрах self, этаж, на который хотим подняться
        if new_floor > self.numbers_of_floor or new_floor <= 0:
            print("Такого этажа не существует!")
        else:
            for i in range(new_floor - 1):
                print(f"Этаж: {i + 1}")
            print(f"Вы на {new_floor} этаже!")
        return None


#Создаём объект house_1
house_1 = House('ЖК Эльбрус', 30)
#Создаём объект house_2
house_2 = House('ЖК Ромашка', 15)

# Тестирование
house_1.go_to(5) #Вывод от 1 до 4, вы на 5 этаже!
house_1.go_to(644) #Такого этажа не существует!
house_1.go_to(-5) #Такого этажа не существует!
print(f"'{house_1.name}' - название дома,\n "
      f"'{house_1.numbers_of_floor}' - количество этажей в доме.\n\n")

house_2.go_to(15) #Вывод от 1 до 14, вы на 15 этаже!
house_2.go_to(-2) #Такого этажа не существует!
house_2.go_to(16) #Такого этажа не существует!
print(f"'{house_2.name}' - название дома,\n "
      f"'{house_2.numbers_of_floor}' - количество этажей в доме.")