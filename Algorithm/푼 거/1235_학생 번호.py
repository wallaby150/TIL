N = int(input())
nums = list(input() for _ in range(N))
l, ans = len(nums[0]), 1
tmp = set()

while l >= ans:
    for num in nums:
        text = num[l-ans:]
        if text not in tmp:
            tmp.add(text)
        else:
            ans += 1
            break
    else:
        break

print(ans)