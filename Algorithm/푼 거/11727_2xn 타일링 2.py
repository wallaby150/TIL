N = int(input())

nums = [1, 3, 5, 11]

for i in range(4, N+1):
    ans = (nums[i-1]+(nums[i-2]*2)) % 10007
    nums.append(ans)

print(nums[N-1])