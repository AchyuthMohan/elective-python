hex_num = input("Enter a hexadecimal number: ")
dec_num = int(hex_num, 16)
bin_num = bin(dec_num)
oct_num = oct(dec_num)

print("Decimal equivalent:", dec_num)
print("Binary equivalent:", bin_num)
print("Octal equivalent:", oct_num)
