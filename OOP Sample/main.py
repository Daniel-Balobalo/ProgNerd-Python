from car import Car

#The OBJECT of the class "Car"
car_1 = Car("Lambo", "Urus", 2020, "Black")

print()
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print()

car_1.drive()
car_1.stop()
print("\n")
