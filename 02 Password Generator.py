# TASK 02  **** PASSWORD GENERATOR **** CODSOFT ****

import random
import string

def create_password(length, complexity):
    char_pool = ""
    
    if complexity >= 1:
        char_pool += string.ascii_lowercase  # Include lowercase letters
    if complexity >= 2:
        char_pool += string.ascii_uppercase  # Include uppercase letters
    if complexity >= 3:
        char_pool += string.digits           # Include digits
    if complexity >= 4:
        char_pool += string.punctuation      # Include special characters
    
    if not char_pool:
        return "Error: Please choose a valid complexity level."
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            pwd_length = int(input("Specify the desired password length: "))
            if pwd_length <= 0:
                print("Password length must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        print("\nChoose the complexity level:")
        print("1. Only lowercase letters")
        print("2. Lowercase and uppercase letters")
        print("3. Letters and numbers")
        print("4. Letters, numbers, and special characters")

        try:
            complexity_level = int(input("Enter complexity level (1-4): "))
            if complexity_level not in [1, 2, 3, 4]:
                print("Invalid choice! Select a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        generated_password = create_password(pwd_length, complexity_level)
        print(f"Your new password is: {generated_password}")

        repeat = input("Generate another password? (yes/no): ").lower()
        if repeat != 'yes':
            print("Thank you for using the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    password_generator()
