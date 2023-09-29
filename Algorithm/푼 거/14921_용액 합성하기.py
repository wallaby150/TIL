import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
solutions = list(map(int, input().split()))
left, right = 0, N-1
ans = solutions[left] + solutions[right]

while left < right:
    tmp = solutions[left] + solutions[right]

    if abs(tmp) < abs(ans):
        ans = tmp

    if tmp > 0:
        right -= 1
    elif tmp < 0:
        left += 1
    else:
        break

print(ans)