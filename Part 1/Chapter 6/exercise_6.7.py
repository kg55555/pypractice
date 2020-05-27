frank = {'first_name': 'frank', 'last_name': 'chen', 'age': 22, 'city': 'surrey'}
eric = {'first_name': "eric", 'last_name': 'wen', 'age': 21, 'city': 'burnaby'}
joy = {'first_name': "joy", 'last_name': 'du', 'age': 22, 'city': 'burnaby'}

people = [frank, eric, joy]

for friend in people:
    print(friend['first_name'], friend['last_name'], friend['age'], friend['city'])