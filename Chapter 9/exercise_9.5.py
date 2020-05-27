class User:

    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        for k, v in kwargs.items():
            setattr(self, k, v)


    def describe_user(self):
         return self.__dict__

    def greeting(self):
        print(f"Hello {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


bob = User('bob', 'jones', age=34)
print(bob.login_attempts)
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
print(bob.login_attempts)
bob.reset_login_attempts()
print(bob.login_attempts)

