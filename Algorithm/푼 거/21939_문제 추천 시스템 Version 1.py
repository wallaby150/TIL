import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
small_q = []
big_q = []
problems = {}
p_l = {}

for _ in range(N):
    p, l = map(int, input().split())
    heapq.heappush(small_q, (l, p))
    heapq.heappush(big_q, (-l, -p))
    problems[(l, p)] = True
    p_l[p] = l

M = int(input())
for _ in range(M):
    order, *nums = input().split()
    if order == 'add':
        p, l = int(nums[0]), int(nums[1])
        heapq.heappush(small_q, (l, p))
        heapq.heappush(big_q, (-l, -p))
        problems[(l, p)] = True
        p_l[p] = l
    elif order == 'solved':
        p = int(nums[0])
        problems[(p_l[p], p)] = False

    # recommend
    else:
        if nums[0] == '1':
            while True:
                l, p = heapq.heappop(big_q)
                if not problems[(-l, -p)]:
                    continue
                print(-p)
                heapq.heappush(big_q, (l, p))
                break
        elif nums[0] == '-1':
            while True:
                l, p = heapq.heappop(small_q)
                if not problems[(l, p)]:
                    continue
                print(p)
                heapq.heappush(small_q, (l, p))
                break
