import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()
ans = set()
L = len(S)

for i in range(L):
    for j in range(i, L):
        ans.add(S[i:j+1])

print(len(ans))