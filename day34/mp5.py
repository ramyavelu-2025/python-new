#task1

for ch in "PYTHON":
    print(ch)

#task2
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


#task3
string = input("Enter a string: ")
reversed_string = ""
for ch in string:
    reversed_string = ch + reversed_string
print("Reversed string:", reversed_string)

#task4
for i in range(1, 21):
    print(i, end=" ")


#task5
for i in range(2, 51, 2):

    print(i, end=" ")


#task6
for i in range(10, 0, -1):
    print(i, end=" ")

#task7  
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

#task8
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i, end=" ")

#task9
for i in range(1, 11):
    if i == 5:
        pass
    else:
        print(i)

#task10
for i in range(1, 11):
    print(i)
else:
    print("Loop finished successfully")

#task11
for index, ch in enumerate("HELLO"):
    print(index, ch)


#task12
sentence = input("Enter a sentence: ")
for index, word in enumerate(sentence.split(), start=1):
    print(index, word)

#task13
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 15)

#task14
while True:
    print("Hello, World!")
    break

#task15
import time
start = time.time()
while True:
    print("Hello, World!")
    if time.time() - start > 5:
        break

#task16
while True:
    text = input("Enter something ('exit' to stop): ")
    if text.lower() == "exit":
        break
    print("You entered:", text)


#task17

i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

#task18
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        continue
    else:
        print("Positive number entered:", num)
        break


#task19
i = 1
while i <= 30:
    if i % 3 != 0:
        print(i, end=" ")
    i += 1


#task20
import random
secret = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("🎉 Correct! You guessed it!")
        break
    else:
        print("❌ Try again.")



#task21
correct_password = "admin123"
while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("✅ Access granted!")
        break
    else:
        print("❌ Wrong password. Try again.")



#task22
correct_pin = "1234"
attempts = 3
while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("✅ Access Granted!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. Attempts left: {attempts}")
if attempts == 0:
    print("🚫 Account Locked.")



#task23     
for i in range(10):
    pass


#task24

for i in range(5):
    pass  # Future code will go here

#task25
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully")


#task26
while True:
    word = input("Enter a word: ")
    if word == "Python":
        print("✅ You entered 'Python'! Loop stopped.")
        break
else:
    print("You never entered 'Python'!")



