class Car:
    default_color = 'grey'
    default_weight = 5000
    def __init__(self, color, model):
        self.color = color
        self.model = model
# абстракция
    def turn_on(self):
        pass
    def info(self):
        print(self.color, self.model)
car_obj_1 = Car('green', 'BMW')
car_obj_2 = Car('red', 'volvo')
car_obj_1.turn_on()
print(car_obj_1.color)
print(car_obj_1.model)
print(car_obj_2.color)
print(car_obj_2.model)
car_obj_1.info()
car_obj_2.info()