from r_user import User
from r_admin import Admin, Privileges

bob = User('bob', 'jones', age=34)
joe = Admin('joe', 'jack', height=160, age=19)
print(joe.describe_user())
joe.privileges.display_privileges()
print(joe.privileges.privileges)
