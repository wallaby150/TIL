import sys
import heapq
sys.stdin = open('11279_최대 힙.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -1 * num)
