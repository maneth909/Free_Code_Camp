import re 
import string
import secrets

def generate_password(length=8, num=1, special_char=1, uppercase=1, lowercase=1):
    numbers = string.digits
    letters = string.ascii_letters
    symbols = string.punctuation

    all_character = numbers + letters + symbols
    
    while True:
        password = ''
        for _ in range (length):
            password += secrets.choice(all_character)

        constraints = [
            (num, r'\d'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]'),
            (special_char, fr'[{symbols}]')
        ]

        if all(
            constraint <= len(re.findall(pattern, password)) 
            for constraint, pattern in constraints):
            break
        # for constraint, pattern in constraints:
        #     if constraint <= len(re.findall(pattern, password)):
        #         break

    return password

if __name__ == '__main__':
    new_password = generate_password(length=8)
    print(new_password)