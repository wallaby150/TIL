import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
count = 0
i, j = 0, N-1

while i < j:
    hap = nums[i] + nums[j]
    if hap == x:
        count += 1
        i += 1
        j -= 1
    elif hap > x:
        j -= 1
    else:
        i += 1

print(count)