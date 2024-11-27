while True:
    nums = list(map(int, input().split()))
    if nums[0] == -1:
        break

    ans = 0
    for n in nums[:-1]:
        if n * 2 in nums[:-1]:
            ans += 1

    print(ans)
