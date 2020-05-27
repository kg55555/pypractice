class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a restaurant that sells {self.type} food")

    def open_restaurant(self):
        print("The restaurant is open")


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavours):
        super().__init__(name, cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print("The available flavours are:")
        for flavour in self.flavours:
            print(flavour)


earnest = IceCreamStand("Earnest's Ice Cream", "Dessert", ['chocolate', 'strawberry', 'mango'])
earnest.show_flavours()
