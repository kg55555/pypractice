add_more, first = True, True
while add_more:
    if first:
        topping = input("What topping would you like to add to your pizza?\n")
    topping = input(f"We have added {topping} to you pizza, what else would you like to add? Type 'quit' to end\n")
    if topping == 'quit':
        break
    else:
        first = False
        add_more = True
print("Thank you for ordering a pizza, we will prepare it shortly")
