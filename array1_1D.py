def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    start = 0
    end = len(s)-1

    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        if s[start] not in vowels:
            start += 1
        if s[end] not in vowels:
            end -= 1

    return "".join(s)       

s = "hello"
output = reverse_vowels(s)
print(output)