# 리스트의 항목 갯수 N, 태수 점수 S, 랭킹 항목 갯수 P
N, S, P = map(int, input().split())

if N:
    nums = list(map(int, input().split()))
    if N == P and nums[-1] >= S:
        print(-1)
    else:
        ans = N + 1
        for i in range(N):
            if nums[i] <= S:
                ans = i + 1
                break
        print(ans)
else:
    print(1)
