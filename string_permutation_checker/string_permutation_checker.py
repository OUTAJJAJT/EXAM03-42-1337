def Anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


print(Anagram("hicham", "chamhi"))
print(Anagram("racecar", "carrace"))
print(Anagram("Conversation", "Voices rant on"))
