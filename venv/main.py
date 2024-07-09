from password_manager import main as manager_main
from generate_password import generate_password

def display_menu():
    print("MasterPass: Password Manager & Generator")
    print("1. Generate Password")
    print("2. Manage Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = display_menu()

        if choice == '1':
            try:
                length = int(input("Enter password length: "))
            except ValueError:
                length = 16  # Default value

            try:
                nums = int(input("Minimum number of digits: "))
            except ValueError:
                nums = 1  # Default value

            try:
                special_chars = int(input("Minimum number of special characters: "))
            except ValueError:
                special_chars = 1  # Default value

            try:
                uppercase = int(input("Minimum number of uppercase letters: "))
            except ValueError:
                uppercase = 1  # Default value

            try:
                lowercase = int(input("Minimum number of lowercase letters: "))
            except ValueError:
                lowercase = 1  # Default value

            password = generate_password(length, nums, special_chars, uppercase, lowercase)
            print(f"Generated password: {password}")
            # No need to call display_menu here, it will be called at the start of the loop
        elif choice == '2':
            manager_main()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()