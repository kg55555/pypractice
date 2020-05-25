#cubes = [num**3 for num in range(1,11)]
cubes = []
for number in range(1,11):
    cubes.append(number**3)
for cube in cubes:
    print(cube)