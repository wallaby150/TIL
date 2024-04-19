import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = [list(map(int, input().split()))for _ in range(N)]
ans = 0

def compare(a, b):
    for k in range(M - 1):
        for l in range(k, M):
            if nums[a][k] > nums[a][l] and nums[b][k] > nums[b][l]:
                continue
            elif nums[a][k] == nums[a][l] and nums[b][k] == nums[b][l]:
                continue
            elif nums[a][k] < nums[a][l] and nums[b][k] < nums[b][l]:
                continue
            else:
                return False
    return True


for i in range(N-1):
    for j in range(i+1, N):
        ans += compare(i, j)

print(ans)