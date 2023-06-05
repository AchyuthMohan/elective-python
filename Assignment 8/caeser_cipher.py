def encrypt(s,n):
    s1=""
    for i in s:
        if i.isupper():
            s1=s1+chr((ord(i)+n-65)%26+65)
        elif i.islower():
            s1=s1+chr((ord(i)+n-97)%26+97)
        else:
            s1=s1+i
    return s1

def decrypt(s,n):
    s1=""
    for i in s:
        if i.isupper():
            s1=s1+chr((ord(i)-n-65)%26+65)
        elif i.islower():
            s1=s1+chr((ord(i)-n-97)%26+97)
        else:
            s1=s1+i
    return s1

s=input("Enter the string: ")
n=int(input("Enter the key: "))
print("Encrypted string: ",encrypt(s,n))
print("Decrypted string: ",decrypt(encrypt(s,n),n))

