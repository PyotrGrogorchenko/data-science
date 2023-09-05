def args(*args):
    return list(filter(lambda x: x is str, args))


print(args(1, '3', 4))