import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
ans = 0

for y in range(N-2):
    now = deque([])
    for j in range(2):
        for i in range(3):
            now.append(nums[y+i][j])

    for x in range(2, M):
        # 리스트에 추가
        for k in range(3):
            now.append(nums[y+k][x])

        if x != 2:
            for _ in range(3):
                now.popleft()

        num = sorted(now)[4]
        if num >= T:
            ans += 1

print(ans)