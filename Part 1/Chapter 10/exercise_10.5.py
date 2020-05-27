while True:
    answer = input("Why do you like programming? Enter 'q' to quit\n")
    if answer == 'q':
        break
    with open('r_programming', 'a') as file_object:
        file_object.write(answer + "\n")