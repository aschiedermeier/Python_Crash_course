from car import Car, ElectricCar

my_new_car = Car("bmw", "X6M", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=23
my_new_car.read_odometer()

my_tesla = ElectricCar("tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()

import car

my_beetle = car.Car("volkswagen","beetle",2018)
print(my_beetle.get_descriptive_name())
my_new_tesla=car.ElectricCar("tesla","roadster",2018)
print(my_new_tesla.get_descriptive_name())