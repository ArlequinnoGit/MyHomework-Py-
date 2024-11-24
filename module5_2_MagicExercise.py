class House: #Создаём класс House
    def __init__(self, name, numbers_of_floor): #Создаём метод __init__, в параметрах указатель self, метода имя и кол-во этажей
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def __len__(self):
        return self.numbers_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floor}'


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

print(house_1.__str__())

print(house_2.__str__())