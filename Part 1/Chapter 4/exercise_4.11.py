pizzas = ['pepperoni', 'canadian', 'pesto']
frpizzas = pizzas[:]
pizzas.append('bacon')
frpizzas.append('ham')
print("My favourite pizzas are:", end=" ")
for pizza in pizzas:
    print(pizza, end=" ")
print("\nMy friend's favourite pizzas are:", end=" ")
for pizza in frpizzas:
    print(pizza, end=" ")