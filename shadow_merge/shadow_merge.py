from typing import List


def mergeList(list1: List[int], list2: List[int]) -> List:
    if list1 is None:
        return sorted(list2)
    if list2 is None:
        return sorted(list1)
    new_list = []
    for i in list1:
        new_list.append(i)
    for j in list2:
        new_list.append(j)
    return sorted(new_list)


print(mergeList(None, [0, 8, 2, 1]))
print(mergeList([99, -22, 10, 9], []))
