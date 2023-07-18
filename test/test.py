def freq_count(s):
    dict = {}
    for i in s:
        if i in dict.keys():
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    dict_list = list(dict.items())
    # x[0] for sort on the basis of key and x[1] for sort on values
    sorted_dict = sorted(dict_list, key=lambda x: x[1])
    sorted_dict = sorted_dict[::-1]
    for i in sorted_dict:
        print(i[0])


s = "Hello World"
freq_count(s)
