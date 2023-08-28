def check_number(num):
    if not isinstance(num, int):
        print('Invalid type')
        return
    print('+') if num > 100 else print('-')

print('99 =')
check_number(99)
print('100 =')
check_number(100)
print('101 =')
check_number(101)
print('"101" =')
check_number('101')
