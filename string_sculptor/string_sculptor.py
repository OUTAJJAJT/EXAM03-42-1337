def string_sculptor(s: str) -> str:
    s1 = s.lower()
    new_s = ""
    counter = 0
    for i in range(len(s1)):
        if s1[i].isalpha():
            if counter % 2 == 0:
                new_s += s1[i]
            elif counter % 2 != 0:
                new_s += s1[i].upper()
            counter += 1
        else:
            new_s += s1[i]
    return new_s


print(string_sculptor("Hello World!"))
print(string_sculptor("123abcDEF"))
print(string_sculptor("a-bC-dEf-ghIj"))
print(string_sculptor("12345"))
