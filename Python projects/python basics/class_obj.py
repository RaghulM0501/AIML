class Car:
    def __init__(self, model,color,engine_type):
        self.model = model
        self.color = color
        self.engine_type = engine_type

    def accelerate(self):
        print(f"The vehicle {self.model} is running")

    def apply_break(self):
        print(f"The vehicle {self.model} is stopped")

car1 = Car("Toyota","White","Diesel")
car2 = Car("Tata","Blue","Petrol")

print(car1.model)
