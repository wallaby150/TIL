import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
hq = []

for i in range(N):
    x, y, v = map(int, input().split())
    cal = (x ** 2 + y ** 2) ** 0.5 / v
    heapq.heappush(hq, (cal, i + 1))

for _ in range(N):
    print(heapq.heappop(hq)[1])
