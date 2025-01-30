words = input()
for char in words:
    i = ord(char) - 3
    if i < ord('A'): i += 26
    print(chr(i), end='')
