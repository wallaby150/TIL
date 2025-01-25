def SumAll(x):
    cnt = 0
    for char in x:
        cnt += int(char)
    return cnt

N = input()
L = len(N)
left, right = N[:L//2], N[L//2:]
ans = bool(SumAll(left) == SumAll(right))

if ans: print("LUCKY")
else: print("READY")
