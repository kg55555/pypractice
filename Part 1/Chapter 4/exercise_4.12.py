my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are: ", end="")
for food in my_foods:
    print(food, end=" ")
print("\nMy friend's favorite foods are: ", end="")
for food in friend_foods:
    print(food, end=" ")