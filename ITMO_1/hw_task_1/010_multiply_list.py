def multiply_list(l):
    i = 0
    while i < len(l):
        l[i] *= i
        i += 1
    return l

print(multiply_list([2, 4, 5, 8, 9, 13]))