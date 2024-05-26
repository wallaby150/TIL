text = input()
ans = ''

for char in text:
    if char.islower():
        ans += chr((ord(char) + 13 - 97) % 26 + 97)
    elif char.isupper():
        ans += chr((ord(char) + 13 - 65) % 26 + 65)
    else:
        ans += char

print(ans)
