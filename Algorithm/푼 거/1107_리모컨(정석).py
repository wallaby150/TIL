N = int(input())
M = int(input())
if M:
    nums = set(map(str, input().split()))

ans = abs(N - 100)
l = len(str(N))

if M:
    for num in range(1000001):
        for char in str(num):
            if char in nums:
                break
        else:
            ans = min(ans, abs(num - N) + len(str(num)))

    print(ans)
else:
    print(min(ans, len(str(N))))