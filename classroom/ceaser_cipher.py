def caesar_cipher(message, shift):
    message = message.upper()
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += shifted_char

        else:
            encrypted_message += char

    return encrypted_message

s=input("Enter the string : ")
n=int(input("Enter the shift value: "))
k=caesar_cipher(s,n)
print(k)