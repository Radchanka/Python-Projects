import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def main():
    """Main function that calls other functions based on user choice."""
    user_choice = input(
        "Type 'weak' to get a weak password, 'medium' to get a medium one, 'strong' to get a strong password: "
    ).lower()

    if user_choice == "weak":
        generate_password(weak=True)
    elif user_choice == "medium":
        generate_password(medium=True)
    elif user_choice == "strong":
        generate_password(strong=True)
    else:
        print(Fore.RED + "Invalid input!")

def generate_password(weak=False, medium=False, strong=False):
    """Generates a password based on the specified complexity."""
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("0123456789")
    symbols = list("~@#$%^&*()?/><|")

    if weak:
        length = int(input("How long should the password be: "))
        password = random.choices(letters, k=length)
    elif medium:
        letter_count = int(input("How many letters in the password: "))
        number_count = int(input("How many numbers in the password: "))
        password = random.choices(letters, k=letter_count) + random.choices(numbers, k=number_count)
        random.shuffle(password)
    elif strong:
        letter_count = int(input("How many letters in the password: "))
        number_count = int(input("How many numbers in the password: "))
        symbol_count = int(input("How many symbols in the password: "))
        password = (
            random.choices(letters, k=letter_count) +
            random.choices(numbers, k=number_count) +
            random.choices(symbols, k=symbol_count)
        )
        random.shuffle(password)

    print("Here is your password: " + Fore.RED + "".join(password))

if __name__ == "__main__":
    main()
