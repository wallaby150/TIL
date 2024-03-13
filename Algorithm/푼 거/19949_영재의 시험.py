nums = list(map(int, input().split()))
tmp = []
ans = 0

def solve(idx):
    global ans

    if idx == 10:
        c = 0
        for i in range(10):
            if tmp[i] == nums[i]:
                c += 1
        if c >= 5:
            ans += 1
        return

    for j in range(1, 6):
        if idx > 1 and tmp[idx-2] == tmp[idx-1] == j:
            continue
        tmp.append(j)
        solve(idx + 1)
        tmp.pop()

solve(0)
print(ans)