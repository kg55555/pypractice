def make_album(name, title, songs=None):
    return {'artist': name, 'album title': title, 'songs': songs}


print(make_album('bob', 'the life'))
print(make_album('joe', 'the dead', 10))
print(make_album('bs2b', 'the 28dhj', 108))

