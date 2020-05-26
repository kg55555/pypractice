def show_messages(texts):
    for text in texts:
        print(text)


def send_messages(texts):
    while texts:
        text = texts.pop()
        print(text)
        sent_messages.append(text)


text_list = ["Hey! :)", "What's up?", "Haha"]
sent_messages = []
# show_messages(text_list[:])
send_messages(text_list[:])
print(text_list, sent_messages)


