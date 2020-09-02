word_freq = {}

text = input("Text: ")
split_text = text.split()

for word in split_text:
    word_freq[word] = word_freq.get(word, 0) + 1

words = list(word_freq.keys())
words.sort()

max_length = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, max_length, word_freq[word]))
