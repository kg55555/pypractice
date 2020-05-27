with open('r_pride', encoding="utf-8") as p:
    pride = p.read()

text = pride.split()
print(len(text))

def word_count(words, match):
    print(words.lower().count(match))

word_count(pride,'the ')