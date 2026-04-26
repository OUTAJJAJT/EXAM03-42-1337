def twister(lists: list[int], n: int) -> list:
    # if not lists:
    #     return []

    # n = n % len(lists)  # handle negative and large n
    return lists[-n:] + lists[:-n]


print(twister([1, 2, 3, 4, 5], 3))
print(twister([1, 2, 3, 4], 2))
print(twister([1, 2, 3, 4, 8], -2))
print(twister([4, 5, 3, 2], 10))
