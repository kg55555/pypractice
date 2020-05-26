favorite_languages = {
   'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'bob': '',
    'joe': ''
}

for name, language in favorite_languages.items():
    if language != '':
        print(f"{name}, your favourite language is {language}")
    else:
        print(f"Please take our language poll, {name}!")
