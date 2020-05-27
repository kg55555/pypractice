glossary = {
    'key': 'A key part of a "key-value" pair',
    'value': 'Can be anything; formally associated with a key',
    'loop': 'Rerunning parts of the code based on a condition',
    'list': 'A collection of values that are not associated with a key',
    'dictionary': 'Equivalent to objects in Java'
}

for word, definition in glossary.items():
    print(word.title())
    print("\t", definition, "\n")