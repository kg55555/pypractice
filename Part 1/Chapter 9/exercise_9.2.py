class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a restaurant that sells {self.type} food")

    def open_restaurant(self):
        print("The restaurant is open")

bob = Restaurant("Bob's Burgers", "American")
joe = Restaurant("Joe's Salami", "Croatian")
steve = Restaurant("Steve's Calamari", "Greek")
joe.describe_restaurant()
steve.describe_restaurant()
bob.describe_restaurant()

