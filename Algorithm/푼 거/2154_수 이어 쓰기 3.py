N = input()
nums = ''.join(map(str, range(1, int(N) + 1)))
print(nums.find(N) + 1)