sentence = input("Enter a sentence: ").strip()
words = sentence.split()
vowel_count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowel_count += 1

print("Original sentence:", sentence)
print("Upper case:", sentence.upper())
print("Title case:", sentence.title())
print("Reversed sentence:", sentence[::-1])
print("Character count:", len(sentence))
print("Word count:", len(words))
print("Vowel count:", vowel_count)

if words:
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    print("Longest word:", longest_word)
else:
    print("No words found in the sentence.")
