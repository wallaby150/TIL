import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = set(map(int, input().split()))
ans = 1


def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for num in nums:
    if prime(num):
        ans *= num

if ans == 1:
    print(-1)
else:
    print(ans)
