sentence = input("Enter a sentence: ")
word_dict = {word: len(word) for word in sentence.split()}
print(word_dict)
