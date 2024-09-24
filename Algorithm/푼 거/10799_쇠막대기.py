import sys
input = lambda: sys.stdin.readline().rstrip()

text = input()
ans = cnt = 0

for i in range(len(text)):
    if text[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if text[i-1] == '(':
            ans += cnt
        else:
            ans += 1
print(ans)