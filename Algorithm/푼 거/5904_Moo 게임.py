N = int(input())
S = 'moo'
ans = [3]
cnt = 0

while ans[-1] < N:
    cnt += 1
    last = ans[-1]
    ans.append(last + cnt + 3 + last)

def recur(n, i):
    if n <= 3:
        return 'xmoo'[n]

    # 왼쪽 편에 있는 거라면
    if n <= ans[i-1]:
        return recur(n, i-1)

    # 중앙에 있는 거라면
    elif n <= ans[i-1] + i + 3:
        if n == ans[i-1] + 1:
            return 'm'
        else:
            return 'o'

    # 오른 편에 있는 거라면
    else:
        return recur(n - ans[i-1] - i - 3, i-1)

print(recur(N, cnt))