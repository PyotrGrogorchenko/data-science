from numpy import sort


def intersection(a, b):
    return list(filter(lambda x: x in b, a))


print(intersection([2, '3', {5}, '1', None, 4], ['3', None, 8, '7', {5}, 7]))
