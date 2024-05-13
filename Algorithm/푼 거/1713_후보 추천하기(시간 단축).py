N = int(input())
input()
nums = list(map(int, input().split()))
ans = {}

for num in nums:
    if ans.get(num):
        ans[num] += 1
    else:
        if len(ans) >= N:
            del(ans[sorted(ans.items(), key=lambda x: x[1])[0][0]])
        ans[num] = 1

print(*sorted(ans.keys()))
