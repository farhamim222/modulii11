# Base class for all cars
class Auto:
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.mileage = 0

    def set_speed(self, speed):
        if speed <= self.top_speed:
            self.current_speed = speed
        else:
            print(f"Cannot set speed to {speed} km/h. Maximum speed is {self.top_speed} km/h.")

    def drive(self, hours):
        distance = self.current_speed * hours
        self.mileage += distance


# Subclass for electric cars
class ElectricCar(Auto):
    def __init__(self, registration_number, top_speed, battery_capacity):
        super().__init__(registration_number, top_speed)
        self.battery_capacity = battery_capacity


# Subclass for combustion engine cars
class CombustionCar(Auto):
    def __init__(self, registration_number, top_speed, tank_size):
        super().__init__(registration_number, top_speed)
        self.tank_size = tank_size


# Main program
def main():
    # Creating an electric car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    electric_car.set_speed(150)  # Set desired speed
    electric_car.drive(3)  # Drive for 3 hours
    print(f"{electric_car.registration_number} mileage: {electric_car.mileage} km")

    # Creating a combustion engine car
    combustion_car = CombustionCar("ACD-123", 165, 32.3)
    combustion_car.set_speed(120)  # Set desired speed
    combustion_car.drive(3)  # Drive for 3 hours
    print(f"{combustion_car.registration_number} mileage: {combustion_car.mileage} km")


# Run the main program
main()

