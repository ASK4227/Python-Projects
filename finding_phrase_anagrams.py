from collections import Counter

# Load the dictionary file
with open("/home/ask/Documents/dict.txt", "r") as file:
    dictionary = file.read().strip().splitlines()  # Read and split by lines into a list

# Get user input word and make it lowercase
word = input("Enter a word: ").lower()

# Create a Counter (letter count) for the input word
word_counter = Counter(word)

# List to store valid words
valid_words = []

limit = len(word)

# Iterate through the dictionary words
for dict_word in dictionary:
    dict_word = dict_word.lower()  # Convert to lowercase for case-insensitive comparison
    dict_word_counter = Counter(dict_word)  # Create a Counter for the dictionary word

    # Check if the dictionary word can be formed from the input word
    if len(dict_word) < limit and all(dict_word_counter[letter] <= word_counter[letter] for letter in dict_word_counter):
        valid_words.append(dict_word)

# Output the valid words (anagrams or words that can be formed from input word)
print(valid_words)
