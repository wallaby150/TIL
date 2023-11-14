import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heap = []

for _ in range(N):
    order = int(input())
    if order == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(order), order))
