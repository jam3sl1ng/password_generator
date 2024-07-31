import random
import string

len = input("How many characters should the password be? ")
caps = input("Should the password have capitals? (yes/no) ")
spec = input("Should the password have special characters and numbers? (yes/no) ")

if caps == "yes":
    letters = string.ascii_letters
else:
    letters = string.ascii_lowercase

if spec == "yes":
    letters = string.ascii_letters + string.digits + string.punctuation
else:
    letters = string.ascii_lowercase

result = ''.join(random.choice(letters) for i in range(int(len)))

print("Your password is: " + result)