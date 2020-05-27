while True:
    name = input("What is your name? Type 'q' to quit\n")
    if name == 'q':
        break
    with open('r_guest_name', 'a') as file_object:
        file_object.write(name + " has visited\n")
    print(f"Welcome {name}!")


