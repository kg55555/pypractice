import json

with open('r_fav') as fn:
    favnum = json.load(fn)

print(f"Your favourite number is {favnum}")

