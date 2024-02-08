from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ans = 0

for i in permutations(nums, N):
    tmp = 0
    for j in range(N-1):
        tmp += abs(i[j] - i[j+1])
    ans = max(ans, tmp)

print(ans)