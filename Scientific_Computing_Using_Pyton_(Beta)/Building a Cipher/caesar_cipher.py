text = 'Hello Zaira'
shift = 3

def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            encrypted_text += new_char
    print('Plain text:', text)
    print('Encypted text:', encrypted_text)

caesar(text, shift)