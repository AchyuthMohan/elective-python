hex_num = input("Enter a two-digit hexadecimal number: ")

binary_num = bin(int(hex_num, 16))[2:].zfill(8)

decimal_num = int(hex_num, 16)

print("The binary equivalent of", hex_num, "is", binary_num)
print("The decimal equivalent of", hex_num, "is", decimal_num)
