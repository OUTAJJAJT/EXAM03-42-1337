def IsValid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False

            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


# Valid cases
print(IsValid("()"))                            # True
print(IsValid("()[]{}"))                        # True
print(IsValid("{[()]}"))                        # True
print(IsValid(""))                              # True  (empty string is valid)
print(IsValid("hello(hhhh)world{ho}w are"))     # True

# Invalid cases
print(IsValid("(]"))           # False
print(IsValid("([)]"))         # False
print(IsValid("((("))          # False
print(IsValid("())"))          # False
print(IsValid("{[(])}"))       # False
