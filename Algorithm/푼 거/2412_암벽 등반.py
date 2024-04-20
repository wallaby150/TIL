import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, T = map(int, input().split())
nums = set()
flag = False

for _ in range(N):
    a, b = map(int, input().split())
    if b == T:
        flag = True
    nums.add((a, b))

if not flag:
    print(-1)
else:
    def dfs():
        q = deque([[0, 0, 0]])

        while q:
            x, y, cnt = q.popleft()

            if y == T:
                return cnt

            for i in range(-2, 3):
                for j in range(-2, 3):
                    tx, ty = x + i, y + j
                    if (tx, ty) in nums:
                        q.append([tx, ty, cnt + 1])
                        nums.remove((tx, ty))

        return -1

    print(dfs())
