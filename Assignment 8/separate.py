def get_positives(x):
    l1=[]
    for i in x:
        if i>0:
            l1.append(i)
    return l1

def get_negatives(x):
    l2=[]
    for i in x:
        if i<0:
            l2.append(i)
    
    return l2

x=list(map(int, input("elements of array: ").strip().split()))
print("Positives: ",get_positives(x))
print("Negatives: ",get_negatives(x))
