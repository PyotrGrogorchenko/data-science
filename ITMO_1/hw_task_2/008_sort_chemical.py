from operator import itemgetter


def sort_chemical(ls):
    return sorted(ls, key=itemgetter(1, 2))


print(sort_chemical([(2, 12, 'Mg'), (1, 11, 'Na'), (1, 3, 'Li'), (2, 4, 'Be')]))
print(sort_chemical([(2, 12, 'a'), (1, 12, 'b'), (1, 3, 'b'), (2, 3, 'a')]))
