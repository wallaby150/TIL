import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
T = int(input())
ans = 0

for y in range(N-2):
    for x in range(M-2):
        now = []
        for i in range(3):
            now += nums[y+i][x:x+3]
        num = sorted(now)[4]
        if num >= T:
            ans += 1

print(ans)