import sys

N = int(input())
target = sum(range(1, N))
nums = sys.stdin.readline()
now = 0
tmp = ""

for num in nums:
    if num.isdigit():
        tmp += num
    else:
        now += int(tmp)
        tmp = ""

if tmp:
    now += int(tmp)
print(now - target)
