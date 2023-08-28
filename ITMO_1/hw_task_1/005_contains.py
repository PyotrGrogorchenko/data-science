def contains(str_1, str_2):
    if not type(str_1) is str or not type(str_2) is str:
        return 'Invalid type'
    return 'NO' if str_1.find(str_2) == -1 else 'YES'

print('"str_1", "str_2" =', contains('str_1', 'str_2'))
print('"str_1", "str" =', contains('str_1', 'str'))
print('121, 12 =', contains(121, 12))