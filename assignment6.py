# create a class for vehicles and inheritance for cars and motorcycle subclass
# brand
# model
# colour
# engine size
# add number of doors
class Vehicle:
    def __init__(self, brand, model, colour, engine_size):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.engine_size = engine_size


class Car(Vehicle):
    def __init__(self, brand, model, colour, engine_size, num_doors):
        super().__init__(brand, model, colour, engine_size)
        self.num_doors = num_doors


class Motorcycle(Vehicle):
    def __init__(self, brand, model, colour, engine_size, num_doors):
        super().__init__(brand, model, colour, engine_size)
        self.num_doors = num_doors


car = Car("Toyota", "Landcruiser 200 Series", "White", "4.5 Litre Diesel", "5 Door")
print(car.brand)
print(car.model)
print(car.colour)
print(car.engine_size)
print(car.num_doors)

motorcycle = Motorcycle("KTM", "KTM RC 390", "White, Black, Orange", "1 Cylinder, 4 Stroke", 0)
print(motorcycle.brand)
print(motorcycle.model)
print(motorcycle.colour)
print(motorcycle.engine_size)
