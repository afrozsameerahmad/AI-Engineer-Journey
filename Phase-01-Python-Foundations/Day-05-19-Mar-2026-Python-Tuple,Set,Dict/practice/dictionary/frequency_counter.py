# Character and word frequency using dictionary
text = "python programming"
char_count = {}
for ch in text:
    if ch != " ":
        char_count[ch] = char_count.get(ch, 0) + 1
print("Character count:", char_count)

sentence = "python is fun and python is easy"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word count:", word_count)

most_common = max(word_count, key=word_count.get)
print("Most common word:", most_common)
