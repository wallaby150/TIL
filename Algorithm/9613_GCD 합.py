import sys
input = lambda : sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

T = int(input())
for _ in range(T):
    ans = 0

    n, *nums = map(int, input().split())
    for i in range(n-1):
        for j in range(i+1, n):
            ans += gcd(nums[i], nums[j])

    print(ans)