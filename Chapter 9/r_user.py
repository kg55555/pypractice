class User:

    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        for k, v in kwargs.items():
            setattr(self, k, v)


    def describe_user(self):
         return self.__dict__

    def greeting(self):
        print(f"Hello {self.first_name}!")
