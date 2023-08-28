def count_days(years, month):
    return (years * 12 + month) * 29


print('1, 1 =', count_days(1, 1))
print('0, 0 =', count_days(0, 0))
print('2, 3 =', count_days(2, 3))

