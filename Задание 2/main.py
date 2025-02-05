class Car:
    def __init__(self, name, brand, color, car_type, year_of_prod, price):
        self.name = name
        self.brand = brand
        self.color = color
        self.car_type = car_type
        self.price = price
        self.year = year_of_prod

    def __str__(self):
        return f"\n{self.name},{self.color}"


bmw_X7 = Car(name="БМВ x7", brand="bmw", color="красный", car_type="хэтчбек", year_of_prod="2015", price=6900000)
bmw_X6 = Car(name="БМВ x6", brand="bmw", color="красный", car_type="седан", year_of_prod="2015", price=6900000)
renault_Clio3 = Car(name="Рено Клио 3", brand="renault", color="зеленый", car_type="хэтчбек", year_of_prod="2009", price=500000)
renault_Logan = Car(name="Рено Логан", brand="bmw", color="красный", car_type="седан", year_of_prod="2015", price=6900000)

my_cars = [bmw_X7, renault_Clio3, bmw_X6, renault_Logan]

new_color=input("Введите цвет для фильтра: ")

def filter_colors(car: Car):
    if car.color == new_color:
        return True
    else:
        return False

carFilter = filter(filter_colors, my_cars)
print(*carFilter)
