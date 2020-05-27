while True:
    num1 = input("Enter the first number\n")
    if num1 == 'q':
        break
    num2 = input("Enter the second number\n")
    if num2 == 'q':
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("One or more of the values that you have entered is not a number!")
        print("Please re-enter your numbers")
        continue
    print(num1 + num2)