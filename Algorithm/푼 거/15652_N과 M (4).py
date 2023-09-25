import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = []

def solve(num, li):
    if len(li) == M:
        ans.append(li)
        return

    for i in range(num, N + 1):
        tmp = li[:]
        tmp.append(i)
        solve(i, tmp)

solve(1, [])
ans.sort()
for a in ans:
    print(" ".join(map(str, a)))