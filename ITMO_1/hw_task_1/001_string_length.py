def get_string_length(s=''):
    if not type(s) is str:
        return 'Invalid type'
    return len(s)

print('"" =', get_string_length(''))
print('"str" =', get_string_length('str'))
print('0 =', get_string_length(0))
