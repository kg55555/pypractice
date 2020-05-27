with open('r_cats') as c:
    cats = c.readlines()

try:
    with open('r_dogs') as d:
        dogs = d.readlines()
except FileNotFoundError:
    pass
else:
    for dog in dogs:
        print(dogs.rstrip())
        
for cat in cats:
    print(cat.rstrip())


