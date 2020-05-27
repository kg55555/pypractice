import json, time

print("We will find your favourite number!")
time.sleep(2)

try:
    with open('r_fav') as fn:
        favnum = json.load(fn)
except FileNotFoundError:
    fav = input("We don't have your favourite number, what is it?\n")
    with open('r_fav', 'w') as fn:
        json.dump(fav, fn)
else:
    print(f"Your favourite number is {favnum}")

