import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    heapq.heapify(nums)
    ans = 0

    while len(nums) >= 2:
        a, b = heapq.heappop(nums), heapq.heappop(nums)
        ans += a + b
        heapq.heappush(nums, a+b)

    print(ans)
