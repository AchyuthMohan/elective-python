my_list = [1, 2, 3, 2, 4, 3, 5, 2, 6, 5]
freq_dict = {}
for num in my_list:
    if num in freq_dict:
        freq_dict[num] += 1
    else:
        freq_dict[num] = 1

max_freq = max(freq_dict.values())
most_common = [num for num, freq in freq_dict.items() if freq == max_freq]

print("The number(s) with the largest frequency of occurrence is/are:", most_common)
