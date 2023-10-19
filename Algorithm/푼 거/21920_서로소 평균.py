import sys, math
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
X = int(input())

# 서로소 리스트
ans = []
check_dict = {}

for a in A:
    if a not in check_dict:
        if math.gcd(a, X) == 1:
            ans.append(a)
            check_dict[a] = True
    else:
        if check_dict[a] == True:
            ans.append(a)

print(sum(ans) / len(ans))