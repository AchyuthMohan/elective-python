plaintext = input("Enter a message to encrypt: ")
shift = 3

ciphertext = ""

for char in plaintext:
    if char.isalpha():
        char_code = ord(char.upper())
        shifted_code = (char_code - 65 + shift) % 26 + 65
        shifted_char = chr(shifted_code)
        ciphertext += shifted_char
    else:
        ciphertext += char
print("The encrypted message is:", ciphertext)
