class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self

    def __radd__(self, value):
        if isinstance(value, House):
            value.number_of_floors += self.number_of_floors
            return value
        elif isinstance(value, int):
            value += self.number_of_floors
            return value

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 += 10 # __iadd__
print(h1)

h2 += 20 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2) # ne