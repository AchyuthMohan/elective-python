dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four"
}
print(dict.get(1))
print(dict)
dict.pop(1)
dict[1]="One"
print(dict[1])
# print(dict.keys())
# print(dict.values())


# traversals
for key in dict.keys():
    print("Value: ",dict.get(key))
print(dict.items())
