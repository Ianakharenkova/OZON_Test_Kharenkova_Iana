class Car:
    def __init__(self, name, brand, color, car_type, manufacture_year, price):
        self.name = name
        self.brand = brand
        self.color = color
        self.car_type = car_type
        self.price = price
        self.year = manufacture_year

    def __str__(self):
        return f"\n{self.name},{self.color}"


bmwX7 = Car(name="BMWx7", brand="bmw", color="red", car_type="hatchback", manufacture_year="2015", price=6900000)
bmwX6 = Car(name="BMWx6", brand="bmw", color="red", car_type="sedan", manufacture_year="2015", price=6900000)
renaultClio3 = Car(name="RenaultClio3", brand="renault", color="green", car_type="hatchback", manufacture_year="2009",
                   price=500000)
renaultLogan = Car(name="renaultLogan", brand="bmw", color="red", car_type="sedan", manufacture_year="2015",
                   price=6900000)

my_cars = [bmwX7, renaultClio3, bmwX6, renaultLogan]

new_color=input("Введите цвет ")

def filter_colors(car: Car):
    if car.color == new_color:
        return True
    else:
        return False

carFilter = filter(filter_colors, my_cars)
print(*carFilter)
