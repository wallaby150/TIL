import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = []
ns = set()
for _ in range(N):
    tmp = int(input())
    nums.append(tmp)
    ns.add(tmp)

nums.sort()

for _ in range(M):
    t = int(input())
    if t in ns:
        print(nums.index(t))
    else:
        print(-1)