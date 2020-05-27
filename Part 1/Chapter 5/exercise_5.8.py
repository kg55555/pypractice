uname = ['admin', 'joe', 'bob', 'steve', 'kled']

for name in uname:
    if name != 'admin':
        print(f"Hello {name}, welcome back!")
    elif name == 'admin':
        print("Welcome back, Admin!")