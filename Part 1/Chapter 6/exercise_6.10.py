bob = [2,6,5]
joe = [9,3,5]
steve = [13,98]
edwin = [23]

favourite_number = {'bob':bob, 'joe':joe,'steve':steve,'edwin':edwin}

for name, numbers in favourite_number.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favourite number is {numbers[0]}")
    elif len(numbers) == 2:
        print(f"{name.title()}'s favourite numbers are {numbers[0]} and {numbers[1]}")
    else:
        numprt = ""
        for counter in range(len(numbers)):
            if counter == len(numbers)-1:
                numprt += "and " + str(numbers[-1])
            else:
                numprt += str(numbers[counter]) + ", "
        print(f"{name.title()}'s favourite numbers are {numprt}")

