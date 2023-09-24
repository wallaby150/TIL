import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()
ans = set()
L = len(S)

for i in range(1, L+1):
    for start in range(L):
        ans.add(S[start:start+i])

print(len(ans))