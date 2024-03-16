N = int(input())
text = input()
l, r = 0, 0
chars = [0] * 26
c = 0
ans = 0

while l <= r and r < len(text):
    r += 1
    char = text[r-1]
    chars[ord(char) - 97] += 1
    if chars[ord(char) - 97] == 1:
        c += 1

    while c > N:
        l += 1
        char = text[l-1]
        chars[ord(char) - 97] -= 1
        if chars[ord(char) - 97] == 0:
            c -= 1

    ans = max(ans, r - l)

print(ans)