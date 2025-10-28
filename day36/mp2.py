# String Manipulation Program

# Take input from user
sentence = input("Enter a sentence: ")

# Perform various string operations
uppercase = sentence.upper()
lowercase = sentence.lower()
title_case = sentence.title()
word_count = len(sentence.split())
char_count = len(sentence)
reversed_sentence = sentence[::-1]
no_spaces = sentence.replace(" ", "")
vowel_count = sum(1 for ch in sentence.lower() if ch in "aeiou")

# Display results in structured format
print("\n" + "=" * 50)
print("📝 STRING MANIPULATION RESULTS")
print("=" * 50)
print(f"Original Sentence  : {sentence}")
print(f"Uppercase          : {uppercase}")
print(f"Lowercase          : {lowercase}")
print(f"Title Case         : {title_case}")
print(f"Word Count         : {word_count}")
print(f"Character Count    : {char_count}")
print(f"Reversed Sentence  : {reversed_sentence}")
print(f"Without Spaces     : {no_spaces}")
print(f"Vowel Count        : {vowel_count}")
print("=" * 50)
