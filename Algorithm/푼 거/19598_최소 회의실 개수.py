import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()
hq = []
ans = 0

for time in times:
    start = time[0]

    while hq:
        now = heapq.heappop(hq)
        if now > start:
            heapq.heappush(hq, now)
            break

    heapq.heappush(hq, time[1])
    ans = max(ans, len(hq))

print(ans)