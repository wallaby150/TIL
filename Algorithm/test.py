import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
ans = [0] * N


def solve(last_num, i, now_sum):
    if i == N:
        return

    ans[i] = max(ans[i-1], ans[i])

    # 지금 추가할 것이나
    if A[i] < last_num:
        if ans[i] < now_sum + A[i]:
            ans[i] = now_sum + A[i]
            solve(A[i], i+1, now_sum + A[i])
    # 마느냐
    solve(last_num, i+1, now_sum)

solve(1001, 0, 0)
# print(ans)
print(ans[-1])