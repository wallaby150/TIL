text = input()
i = 0
vowels = {'a', 'e', 'i', 'o', 'u'}

while i < len(text):
    print(text[i], end='')
    if text[i] in vowels:
        i += 2
    i += 1