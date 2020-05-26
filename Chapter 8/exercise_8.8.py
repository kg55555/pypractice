def make_album(name, title, songs=None):
    return {'artist': name, 'album title': title, 'songs': songs}


print("Create an album!")

while True:
    artist = input("Enter the artist name\n")
    album = input("Enter the album title\n")
    song_num = input("Enter the number of songs\n")
    print(make_album(artist, album, song_num))
    if input("Press any key to restart, 'q' to quit\n") == 'q':
        break


