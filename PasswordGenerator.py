import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
            else:
                password = generate_password(length)
                print("Generated Password:", password)
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
