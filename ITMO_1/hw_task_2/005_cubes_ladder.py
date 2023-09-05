from functools import reduce


def cubes_ladder(n):
    dp = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - j][j - 1] + 1

    return reduce(lambda x, y: x + y, dp[n])


print('1 -', cubes_ladder(1))
print('2 -', cubes_ladder(2))
print('3 -', cubes_ladder(3))
print('4 -', cubes_ladder(4))
print('5 -', cubes_ladder(5))
print('6 -', cubes_ladder(6))
print('7 -', cubes_ladder(7))
print('8 -', cubes_ladder(8))
print('9 -', cubes_ladder(9))
print('10 -', cubes_ladder(10))
print('100 -', cubes_ladder(100))
