import random
import string

def generatepwd(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meet_criteria = True

        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


min_length = input("Enter the minimum length: ")
numbers = input("Does the password require numbers?(y/n): ")
special_characters = input("Does the password require special characters? (y/n): ")
valid_inputs = ['y', 'n']

while numbers not in valid_inputs or special_characters not in valid_inputs or not min_length.isdigit(): # Handle error cases
    print("Invalid input")
    min_length = input("Enter the minimum length: ")
    numbers = input("Does the password require numbers?(y/n): ")
    special_characters = input("Does the password require special characters? (y/n): ")


pwd = generatepwd(int(min_length), numbers, special_characters)
print(f"Password: {pwd}")
         
