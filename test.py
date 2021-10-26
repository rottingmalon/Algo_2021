def maxsearch(list):
    if (len(list) == 1):
        return (list[0])
    first = list[0]
    max = maxsearch(list[1:])
    if (first < max):
        return (max)
    else:
        return (first)

print (maxsearch([1, 89, 12, 55]))