N = input()
l = len(N) - 1
ans = 0

for i in range(l):
    ans += 9 * (10 ** i) * (i + 1)

ans += ((int(N) - (10 ** l)) + 1) * (l + 1)
print(ans)
