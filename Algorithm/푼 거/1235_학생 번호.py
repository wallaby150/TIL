N = int(input())
nums = list(input() for _ in range(N))
result = 0
l = len(nums[0])

for i in range(1, l):
    c = set()
    for num in nums:
        c.add(num[-i:])
    if len(c) == N:
        ans = i
        break

print(ans)