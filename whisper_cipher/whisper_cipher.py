def get_index(character: str) -> int:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alpha)):
        if character == alpha[i]:
            return i
        if character == ALPHA[i]:
            return i
    return -1


def Shift_alphabet(s: str, shift: int) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for i in range(len(s)):
        if s[i].isalpha():
            index = get_index(s[i])
            new_index = (index + shift) % 26
            if s[i].isupper():
                result += ALPHA[new_index]
            elif s[i].islower():
                result += alpha[new_index]
        else:
            result += s[i]

    return result


print(Shift_alphabet("HeLlo world", 3))