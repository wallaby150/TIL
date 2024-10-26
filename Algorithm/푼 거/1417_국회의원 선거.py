import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
win = int(input())
nums = []
ans = 0

for _ in range(N-1):
    heapq.heappush(nums, -int(input()))

while nums:
    num = -heapq.heappop(nums)
    if num >= win:
        num -= 1
        win += 1
        ans += 1
        heapq.heappush(nums, -num)

print(ans)
