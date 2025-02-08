N = int(input())
nums = list(map(int, input().split()))
budget = int(input())
high, low = max(nums), 0
ans = 0

if sum(nums) <= budget:
    print(high)
else:
    while low <= high:
        m = (high + low) // 2
        use = sum(min(num, m) for num in nums)

        if use > budget:
            high = m - 1
        else:
            ans = m
            low = m + 1

    print(ans)
