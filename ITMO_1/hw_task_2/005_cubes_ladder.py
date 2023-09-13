def cubes_ladder(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            dp[j] += dp[j - i]
    return dp[n]


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
print('13 -', cubes_ladder(13))
print('14 -', cubes_ladder(14))
print('15 -', cubes_ladder(15))
print('16 -', cubes_ladder(16))
print('29 -', cubes_ladder(29))
print('100 -', cubes_ladder(100))
