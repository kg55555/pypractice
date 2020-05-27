import json

fav = input("What is your favourite number?\n")

with open('r_fav', 'w') as fn:
    json.dump(fav, fn)

