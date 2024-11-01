N = int(input())
nums = sorted(list(map(int, input().split())))
stick = sum(nums)
answer = 0

for num in nums:
    answer += num * (stick - num)
    stick -= num

print(answer)