N = int(input())
nums = list(map(int, input().split()))

print(1)
for i in range(2, min(nums) + 1):
    for num in nums:
        if num % i:
            break
    else:
        print(i)