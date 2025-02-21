T = int(input())
N = list(map(int, input().split()))

nums = [0] * 80001
cnt = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        cnt += i
    nums[i] = cnt

for num in N:
    print(nums[num])