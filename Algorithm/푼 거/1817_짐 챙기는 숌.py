N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    nums = list(map(int, input().split()))
    cnt, weight = 1, 0
    for num in nums:
        if weight + num <= M:
            weight += num
        else:
            weight = num
            cnt += 1
    print(cnt)
