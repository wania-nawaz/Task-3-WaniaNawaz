"""
Project 3: Random Password Generator
DecodeLabs - Python Programming Industrial Training Kit

Description:
    A secure password generator that uses Python's 'secrets' module
    (cryptographically strong) instead of the 'random' module,
    combined with the 'string' module for character set management.

Key Skills Demonstrated:
    - Module Integration (secrets, string)
    - String Manipulation
    - Input Validation
    - Efficient String Building (str.join)
"""

import secrets
import string


def get_valid_length():
    """Prompt the user for a password length and validate the input."""
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Password length must be at least 4 characters. Please try again.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_password(length):
    """Generate a cryptographically secure random password of the given length."""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols

    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    remaining_length = length - len(password_chars)
    password_chars += [secrets.choice(all_characters) for _ in range(remaining_length)]

    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


def main():
    print("=" * 45)
    print("     DecodeLabs Random Password Generator")
    print("=" * 45)

    length = get_valid_length()
    password = generate_password(length)

    print("\nGenerated Password:", password)
    print("Length:", len(password), "characters")


if __name__ == "__main__":
    main()
