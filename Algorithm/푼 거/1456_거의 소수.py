A, B = map(int, input().split())
cnt = 0

prime = [False, False] + [True] * (int(B ** 0.5) - 1)
for i in range(2, (int(B ** 0.5) + 1)):
    # 소수라면
    if prime[i]:
        for j in range(i * 2, (int(B ** 0.5)) + 1, i):
            prime[j] = False

for k in range(2, int(B ** 0.5) + 1):
    if prime[k]:
        tmp = k * k
        while tmp <= B:
            if A <= tmp:
                cnt += 1
            tmp *= k

print(cnt)
