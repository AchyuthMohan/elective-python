def cipher_gen(s, key):
    res = ''
    for i in s:
        if i.isalpha():  # Check if the character is a letter
            if i.isupper():
                base = ord('A')
            else:
                base = ord('a')
            order = ord(i) - base
            target = (order + key) % 26
            letter = chr(target + base)
        else:
            letter = i
        res += letter
    return res

s = "Hello World"
key = 2
res = cipher_gen(s, key)
print(res)
