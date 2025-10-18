# Program to count word frequency in a sentence

# Take input from user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase for consistency
sentence = sentence.lower()

# Split sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the results
print("\nWord Frequency Count:")
print("-" * 25)
for word, count in word_count.items():
    print(f"{word:<10} : {count}")
