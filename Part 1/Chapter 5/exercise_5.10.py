current_users = ['admin', 'joe', 'bob', 'steve', 'kled']
new_users = ['rogan', 'joe', 'kled', 'thomas', 'steven']

for user in new_users:
    if user in current_users:
        print(f"{user}, This username has been taken, please select a new username")
    else:
        print(f"{user}, this username is available")