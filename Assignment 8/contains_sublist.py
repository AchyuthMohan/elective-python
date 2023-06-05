def contains_sublist(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[0]:
            if list1[i:i+len(list2)] == list2:
                return True
    return False

l1=input("Enter the list1: ").split()
l2=input("Enter the list2: ").split()
print(contains_sublist(l1,l2))