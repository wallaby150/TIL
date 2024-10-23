N, P = map(int, input().split())
nums = []
num = N

while True:
    num = num * N % P

    if num in nums:
        print(len(nums[nums.index(num):]))
        break

    nums.append(num)