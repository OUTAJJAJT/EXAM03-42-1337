from typing import List


def reverseMatrix(s: List[List[int]]) -> List[List[int]]:
    return [e[::-1] for e in s]


input = [
    [1, 2, 3],
    [2, 5, 9],
    [10, 20, 30]
    ]
print(reverseMatrix(input))
