from functools import reduce


def multiplicity(nums, divider=0):
    if divider == 0:
        return []

    return list(filter(lambda x: x % divider == 0, nums))


print(multiplicity([1, 2, 3, 4, 5], 2))
print(multiplicity([1, 2, 3, 4, 5], 0))
print(multiplicity([]))
