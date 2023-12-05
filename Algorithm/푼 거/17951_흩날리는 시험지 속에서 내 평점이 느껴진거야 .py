import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
l, r = 0, N//K*20 + 1

while l <= r:
    mid = (l + r) // 2
    group = 0
    score = 0
    flag = False

    for num in nums:
        score += num

        if score >= mid:
            score = 0
            group += 1

            if group == K:
                flag = True
                break

    if flag:
        l = mid + 1
        answer = mid

    else:
        r = mid - 1

print(answer)