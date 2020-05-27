sandwich_orders = ['tuna', 'ham', 'blt', 'cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("we have run out of pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich != 'pastrami':
        print(f"I made your {current_sandwich} sandwich")
        finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)