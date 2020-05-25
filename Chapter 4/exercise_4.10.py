cubes = [num**3 for num in range(1,11)]
for cube in cubes:
    print(cube)
print("The first 3 items in the list are", cubes[:3])
print("The middle 3 items in the list are", cubes[3:6])
print("The first 3 items in the list are", cubes[-3:])