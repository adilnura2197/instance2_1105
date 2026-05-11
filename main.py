class Car:
    wheels = 4
    country = "Germany"

    def __init__(self, brand, color, price, speed):
        self.brand = brand
        self.color = color
        self.price = price
        self.speed = speed

    def show_car(self):
        print(f"""
Brand: {self.brand}
Color: {self.color}
Price: {self.price}
Speed: {self.speed} km/h
Wheels: {Car.wheels}
Country: {Car.country}
""")

    def change_color(self, new_color):
        self.color = new_color

    def increase_speed(self, km):
        self.speed += km


car1 = Car("BMW", "Black", 50000, 220)
car2 = Car("Mercedes", "White", 60000, 240)

print("=== OLD DATA ===")
car1.show_car()
car2.show_car()

car1.change_color("Red")
car1.increase_speed(20)

car2.change_color("Blue")
car2.increase_speed(30)

print("=== NEW DATA ===")
car1.show_car()
car2.show_car()
