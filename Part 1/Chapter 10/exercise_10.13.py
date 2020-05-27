import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'r_user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'r_user.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def check_username(user):
    while True:
        check = input(f"Is {user} your username? y/n\n")
        if check.lower() == 'y':
            break
        elif check.lower() == 'n':
            user = get_new_username()
            break
    return user

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        username = check_username(username)
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
