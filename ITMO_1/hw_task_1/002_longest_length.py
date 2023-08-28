def get_longest_length(list_a, list_b):
    try:
        if len(list_a) > len(list_b):
            return len(list_a)
        return len(list_b)
    except Exception as err:
        return err

print('[1, 2], [1, 2, 3] =', get_longest_length([1, 2], [1, 2, 3]))
print('[1, 2, 3], [1, 2] =', get_longest_length([1, 2, 3], [1, 2]))
print('[], [] =', get_longest_length([], []))
print('"a", [] =', get_longest_length('a', []))
print('"a", 2 =', get_longest_length('a', 2))
