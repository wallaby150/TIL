import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
beers = list(list(map(int, input().split())) for _ in range(K))
beers = sorted(beers,key=lambda x: (x[1],x[0]))

p = 0
heap = []

for beer in beers:
    p += beer[0]
    heapq.heappush(heap, beer[0])

    if len(heap) == N:
        if p >= M:
            answer = beer[1]
            break
        else:
            p -= heapq.heappop(heap)
else:
    print(-1)
    exit()

print(answer)