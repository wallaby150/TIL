import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
needs = [int(input()) for _ in range(N)]
needs_set = set(needs)
ans = 0

while needs_set:
    x = needs_set.pop()
    now = ''
    count = 0

    for need in needs:
        if need == x:
            continue

        elif now == '':
            now = need
            count += 1

        elif now == need:
            count += 1

        else:
            ans = max(count, ans)
            now = need
            count = 1
    ans = max(count, ans)

print(ans)