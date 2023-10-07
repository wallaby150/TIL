import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
ans = []


def solve(result, l):
    if n == result:
        ans.append(l)
        return

    for i in range(1, 4):
        if result + i > n:
            break

        solve(result + i, l + [i])

solve(0, [])

if len(ans) >= k:
    print('+'.join(map(str, sorted(ans)[k-1])))
else:
    print(-1)
