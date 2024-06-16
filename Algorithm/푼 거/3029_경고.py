nt = list(map(int, input().split(":")))
tt = list(map(int, input().split(":")))

if nt == tt:
    print("24:00:00")
    exit()

ans = [0, 0, 0]

for i in range(2, -1, -1):
    if nt[i] > tt[i]:
        if i != 0:
            ans[i] = str(60 - nt[i] + tt[i]).zfill(2)
            nt[i-1] += 1
        else:
            ans[i] = str(24 - nt[i] + tt[i]).zfill(2)
    else:
        ans[i] = str(tt[i] - nt[i]).zfill(2)

print(':'.join(ans))
