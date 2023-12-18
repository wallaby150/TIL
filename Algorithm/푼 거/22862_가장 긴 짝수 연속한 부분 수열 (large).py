import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))

s, e = 0, 0
odd, even = 0, 0
answer = 0


while e < N:
    # 짝수이면
    if nums[e] % 2 == 0:
        even += 1
        answer = max(even, answer)
    else:
        odd += 1
        while odd > K:
            if nums[s] % 2 == 0:
                even -= 1
            else:
                odd -= 1
            s += 1
    e += 1

print(answer)
