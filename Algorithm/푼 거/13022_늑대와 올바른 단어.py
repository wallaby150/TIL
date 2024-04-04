import sys
input = lambda : sys.stdin.readline().rstrip()

word = input()
cnt = [0, 0, 0]
ans = 1


for char in word:
    if char == 'w':
        if sum(cnt[1:]):
            ans = 0
            break
        else:
            cnt[0] += 1
    elif char == 'o':
        if not cnt[0] or cnt[2]:
            ans = 0
            break
        else:
            cnt[0] -= 1
            cnt[1] += 1
    elif char == 'l':
        if not cnt[1] or cnt[0]:
            ans = 0
            break
        else:
            cnt[1] -= 1
            cnt[2] += 1
    else:
        if not cnt[2] or sum(cnt[:2]):
            ans = 0
            break
        else:
            cnt[2] -= 1
else:
    if sum(cnt):
        ans = 0

print(ans)
