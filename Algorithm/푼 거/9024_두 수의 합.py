import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, K = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    mini = 200000000

    for i in range(N-1):
        l = i + 1
        r = N - 1

        while l <= r:
            mid = (l + r) // 2
            tmp = nums[i] + nums[mid]

            if tmp > K:
                r = mid - 1
            else:
                l = mid + 1

            if abs(K-tmp) < mini:
                cnt = 1
                mini = abs(K-tmp)

            elif abs(K-tmp) == mini:
                cnt += 1

    print(cnt)