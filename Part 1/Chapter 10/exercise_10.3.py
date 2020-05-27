name = input("What is your name\n")

with open('r_guest_name', 'w') as file_object:
    file_object.write(name)
