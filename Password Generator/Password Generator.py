import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a valid length greater than zero.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

