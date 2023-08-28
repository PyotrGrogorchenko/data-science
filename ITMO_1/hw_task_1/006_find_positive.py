def find_positive(nums):
    res = 0
    for num in nums:
        if num > 0:
            res += 1
    return res

print('[1, 2, 3, 4, 5] =', find_positive([1, 2, 3, 4, 5]))
print('[1, -2, -3, 4, 5] =', find_positive([1, -2, -3, 4, 5]))