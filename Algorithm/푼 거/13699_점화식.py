N = int(input())
ans = [1, 1]

for i in range(2, N+1):
    tmp = 0
    for j in range(i):
        tmp += ans[j] * ans[i-1-j]
    ans.append(tmp)

print(ans[N])
