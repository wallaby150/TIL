import math

N = int(input())
nums = list(map(int, input().split()))

if N == 2:
    ans = math.gcd(nums[0], nums[1])
else:
    ans = math.gcd(nums[0], math.gcd(nums[1], nums[2]))

small_divisors = []
large_divisors = []

for i in range(1, int(math.sqrt(ans)) + 1):
    if ans % i == 0:
        small_divisors.append(i)  # 작은 약수는 바로 추가
        if i != ans // i:
            large_divisors.append(ans // i)  # 대칭 약수는 따로 추가

for divisor in small_divisors + large_divisors[::-1]:  # 큰 약수 리스트는 역순으로 출력
    print(divisor)
