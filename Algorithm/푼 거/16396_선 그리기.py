import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

total_length = 0
start, end = -1, -1

for s, e in lines:
    if s > end:
        total_length += end - start
        start, end = s, e
    else:
        end = max(end, e)

total_length += end - start  # 마지막 선분 추가
print(total_length)
