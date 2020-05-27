while True:
    num1 = input("Enter the first number\n")
    try:
        num1 = int(num1)
    except ValueError:
        print("The value you have entered is not a number!")
        continue
    num2 = input("Enter the second number\n")
    try:
        num2 = int(num2)
    except ValueError:
        print("The value you have entered is not a number!")
        continue
    print(num1 + num2)