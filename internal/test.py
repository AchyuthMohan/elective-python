with open('sample.txt', 'r') as file:
    message = file.read()
def shift_cipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message = message.lower()
    encrypted_message = ''
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + key) % 26
            shifted_char = alphabet[shifted_index]
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message
encrypted_message = shift_cipher(message, 3)
with open('enc.txt', 'w') as file:
    file.write(encrypted_message)
