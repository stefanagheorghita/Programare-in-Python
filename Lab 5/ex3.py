class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:", self.make, "|", "Model:", self.model, "|", "Year:", self.year)


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

    def display_info(self):
        print("Make:", self.make, "|", "Model:", self.model, "|", "Year:", self.year, "|", "Fuel efficiency:",
              self.fuel_efficiency)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

    def display_info(self):
        print("Make:", self.make, "|", "Model:", self.model, "|", "Year:", self.year, "|", "Fuel efficiency:",
              self.fuel_efficiency)


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity, fuel_efficiency):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity
        self.fuel_efficiency = fuel_efficiency

    def calculate_towing_capacity(self):
        return self.towing_capacity

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

    def display_info(self):
        print("Make:", self.make, "|", "Model:", self.model, "|", "Year:", self.year, "|", "Towing capacity:",
              self.towing_capacity, "|", "Fuel efficiency:", self.fuel_efficiency)


class Bicycle(Vehicle):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("BMW", "X4", 2015, 25)
car.display_info()
print("Mileage:", car.calculate_mileage(100), "miles")

motorcycle = Motorcycle("Harley-Davidson", "123f", 2020, 50)
motorcycle.display_info()
mileage = motorcycle.calculate_mileage(100)
print("Mileage:", mileage, "miles")

bicycle = Bicycle("Giant", "Defy", 2021)
bicycle.display_info()

truck = Truck("DAF", "150", 2022, 8000, 20)
truck.display_info()
towing_capacity = truck.calculate_towing_capacity()
print("Towing capacity:", towing_capacity, "pounds")
mileage = truck.calculate_mileage(100)
print("Mileage:", mileage, "miles")
