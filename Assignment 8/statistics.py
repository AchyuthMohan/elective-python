def mean(x):
    s = 0
    for i in x:
        s = s+i
    return s/len(x)


def median(x):
    x.sort()
    if len(x) % 2 == 0:
        return (x[len(x)//2]+x[(len(x)//2)-1])/2
    else:
        return x[len(x)//2]


def mode(x):
    x.sort()
    d = {}
    for i in x:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
            m = i
    return m


def main():
    x = [int(i) for i in input("Enter the numbers: ").split()]
    print("Mean: ", mean(x))
    print("Median: ", median(x))
    print("Mode: ", mode(x))


main()
