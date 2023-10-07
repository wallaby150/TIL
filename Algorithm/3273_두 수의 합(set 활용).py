import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = set(map(int, input().split()))
x = int(input())
count = 0

for num in nums:
    if x - num in nums:
        count += 1

print(count // 2)
