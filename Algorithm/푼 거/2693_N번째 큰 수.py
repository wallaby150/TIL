T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    print(sorted(nums)[-3])