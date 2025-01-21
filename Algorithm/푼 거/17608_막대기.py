import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
nums = list(int(input()) for _ in range(T))
high, cnt = 0, 0

for i in range(T):
    x = nums[T-i-1]
    if x > high:
        high = x
        cnt += 1

print(cnt)