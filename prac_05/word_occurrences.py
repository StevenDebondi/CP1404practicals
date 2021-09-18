"""
CP1404 Practical
Word Occurrences in a string
"""

words_dict = {}
text = input("Text: ")

words = text.split()
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

words = list(words_dict.keys())
words.sort()

longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, longest_word, words_dict[word]))
