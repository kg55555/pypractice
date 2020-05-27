class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} is a restaurant that sells {self.type} food")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, customer):
        self.number_served = customer

    def increment_number_served(self, customer):
        self.number_served += customer


restaurant = Restaurant("Bob's Burgers", "American")
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(12)
print(restaurant.number_served)