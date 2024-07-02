text = 'Hello Zaira'
key = 'python'

def vigenere(text, key, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = ''
    key_index = 0
    for char in text.lower():
        if char == ' ':
            cipher_text += char
        else:
            #access key one by one
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (offset*direction +index) % len(alphabet)

            #find and append cipher char
            new_char = alphabet[new_index]
            cipher_text += new_char
    return cipher_text

encryption = vigenere(text, key, 1)
print(encryption)

decryption = vigenere(encryption,key,-1)
print(decryption)