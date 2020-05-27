from r_user import User

class Admin(User):

    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges()



class Privileges:

    def __init__(self):
        self.privileges = ['can edit posts', 'can delete posts', 'can ban user']

    def display_privileges(self):
        print("Your admin privileges are:")
        for privilege in self.privileges:
            print(privilege)