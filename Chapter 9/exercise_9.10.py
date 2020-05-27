from r_restaurant import Restaurant

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
earnest.open_restaurant()
earnest.describe_restaurant()
