n = int(input())
tmp = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for i in range(n):
    tmp[i] -= b
    ans += 1
    if tmp[i] > 0:
        if tmp[i] % c == 0:
            ans += (tmp[i] // c)
        else:
            ans += (tmp[i] // c + 1)

print(ans)
