def add_to_list(l, value):
    if not type(l) is list:
        return 'Invalid list type'
    l.append(value)
    return l

_arr = []
print(add_to_list(_arr, 'str'))
print(add_to_list(_arr, [0]))
print(add_to_list(_arr, None))
print(add_to_list('str', 1))