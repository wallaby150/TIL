import heapq
import sys
sys.stdin = open("7662_이중 우선순위 큐.txt")
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for tc in range(T):
    K = int(input())
    heap = []

    for _ in range(K):
        operator, n = map(str, input().split())
        n = int(n)

        if operator == 'I':
            heapq.heappush(heap, n)
        # operator == 'D'
        else:
            if len(heap) == 0:
                pass
            else:
                if n == 1:
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                # n == -1:
                else:
                    heapq.heappop(heap)

    if heap:
        print(heapq.nlargest(1, heap)[0], heap[0])
    else:
        print('EMPTY')


'''
EMPTY
333 -45
'''