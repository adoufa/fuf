class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def a(self):
        return("Автомобиль заведен")
    def b(self):
        return(" Отключение автомобиля")
    def s(self):
        return self.year
    def t(self):
        return self.type
    def r(self):
        return self.color
c = Car("White", "passenger", 2018)
print(c.a())
print(c.b())
print(c.r())
print(c.t())
print(c.s())