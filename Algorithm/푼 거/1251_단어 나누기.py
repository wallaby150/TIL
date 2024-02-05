text = input()
ans = 'z' * 50

l = len(text)
for i in range(1, l-1):
    for j in range(i+1, l):
        tmp = text[:i][::-1] + text[i:j][::-1] + text[j:][::-1]
        if ans > tmp:
            ans = tmp

print(ans)