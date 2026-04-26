from typing import List


def cryptic_sorter(tlist: List[str]):
    def counting(s):
        counter = 0
        for i in s.lower():
            if i in "aeiou":
                counter += 1
        return counter
    final_list = sorted(tlist, key=lambda s: (len(s), s.lower(), s.isupper(), counting(s)))
    return final_list


print(cryptic_sorter(["apple", "bat", "car", "ae", "b"]))