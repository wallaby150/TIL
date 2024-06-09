import heapq

N = int(input())
nums = []

for _ in range(N):
    for num in map(int, input().split()):
        heapq.heappush(nums, num)

    while len(nums) > N:
        heapq.heappop(nums)

print(heapq.heappop(nums))
