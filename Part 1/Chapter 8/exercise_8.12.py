def make_sandwich(*args):
    print("These ingredients are in your sandwich:")
    for arg in args:
        print(f"- {arg}")


sandwich = ['lettuce', 'tomatoe', 'rocks']
make_sandwich('lettuce', 'tomatoe', 'potatoe', 'spinach')
make_sandwich('olives', 'ham')
make_sandwich(*sandwich)
