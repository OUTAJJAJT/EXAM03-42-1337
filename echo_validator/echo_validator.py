def is_palindrome(s: str) -> bool:
    reversed_string = ""
    i = 0
    while i < len(s):
        if s[i].isalnum():
            reversed_string += s[i].lower()
        i += 1
    return reversed_string == reversed_string[::-1]


print(is_palindrome("madam"))
print(is_palindrome("race a car"))
print(is_palindrome("A man nama"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Able was I ere I saw Elba"))  # True