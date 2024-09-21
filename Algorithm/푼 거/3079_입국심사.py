import sys
input = lambda : sys.stdin.readline().rstrip()

# 입국심사대 갯수 N, 사람 수 M
N, M = map(int, input().split())
nums = sorted([int(input()) for _ in range(N)])
ans = -1

l, r = 1, nums[0] * M + 1

while l <= r:
    # 소요시간 m
    m = (l + r) // 2
    cnt = 0

    for num in nums:
        cnt += m // num
        if cnt >= M:
            r = m - 1
            ans = m
            break
    else:
        l = m + 1

print(ans)
