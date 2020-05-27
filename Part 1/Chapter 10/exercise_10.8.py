with open('r_cats') as c:
    cats = c.readlines()

try:
    with open('r_dogs') as d:
        dogs = d.readlines()
except FileNotFoundError:
    print("Sorry the file was not found")
else:
    for dog in dogs:
        print(dogs.rstrip())

for cat in cats:
    print(cat.rstrip())


