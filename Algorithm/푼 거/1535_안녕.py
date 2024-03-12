N = int(input())

losses = list(map(int, input().split()))
gains = list(map(int, input().split()))
total = []
ans = 0

for i in range(N):
    total.append([gains[i], losses[i]])

total.sort(key=lambda x : (x[1], -x[0]))


def solve(idx, gain, heart):
    global ans

    if idx == N or heart <= total[idx][1]:
        ans = max(ans, gain)
        return

    for i in range(idx, N):
        now_gain, now_loss = total[i][0], total[i][1]
        if heart > now_loss:
            solve(i + 1, gain + now_gain, heart - now_loss)
        else:
            break
    return


solve(0, 0, 100)
print(ans)