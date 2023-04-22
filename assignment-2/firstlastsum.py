def num_to_words(num):
    word_dict = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
    }
    num_str = str(num)

    words = []
    for digit in num_str:
        words.append(word_dict[digit])

    print(" ".join(words))


num = int(input("Enter the number: "))
num_to_words(num)
