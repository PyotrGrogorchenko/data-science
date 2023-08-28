def factorial(num):
    if num < 2:
        return 1;
    res = 1
    for n in range(2, num+1):
        res *= n
    return res

print('0 =', factorial(0))
print('1 =', factorial(1))
print('2 =', factorial(2))
print('3 =', factorial(3))
print('6 =', factorial(6))