text = input("Enter a sentence:")
words = text.split()
word_dict = {}
for i in words:
    if i not in word_dict:
        word_dict[i] = 1
    else:
        word_dict[i] = word_dict[i] + 1

word_list=word_dict()


