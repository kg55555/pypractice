famous = ['steve jobs', 'bill gates', 'gandhi']
print(f"Hello {famous[0].title()}, I'd like to invite you to dinner with me!")
print(f"Hello {famous[1].title()}, I'd like to invite you to dinner with me!")
print(f"Hello {famous[2].title()}, I'd like to invite you to dinner with me!")
print(f"Oh no! {famous.pop().title()} is dead, so he can't make it to dinner, I'll invite Elon Musk instead")
famous.append("elon musk")
print(f"Hello {famous[2].title()}, I'd like to invite you to dinner with me!")
print("I found a bigger dinner table!")
famous.insert(0, 'bobby jones')
famous.insert(2, 'tim cook')
famous.append('jesus')
for person in famous:
    print(f"Hello {person.title()}, I'd like to invite you to dinner with me!")
