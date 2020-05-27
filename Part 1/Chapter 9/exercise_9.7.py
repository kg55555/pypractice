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

class Admin(User):

    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = ['can edit posts', 'can delete posts', 'can ban user']


    def  display_privileges(self):
        print("Your admin privileges are:")
        for privilege in self.privileges:
            print(privilege)

bob = User('bob', 'jones', age=34)
joe = Admin('joe', 'jack', height=160, age=19)
print(joe.describe_user())
joe.display_privileges()
