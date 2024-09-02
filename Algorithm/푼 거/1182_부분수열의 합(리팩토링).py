def count_subsequences(idx, current_sum):
    if idx == N:
        return 1 if current_sum == S else 0

    # 현재 수를 포함하지 않는 경우와 포함하는 경우의 합
    count_with_current = count_subsequences(idx + 1, current_sum + nums[idx])
    count_without_current = count_subsequences(idx + 1, current_sum)

    return count_with_current + count_without_current


N, S = map(int, input().split())
nums = list(map(int, input().split()))
result = count_subsequences(0, 0)

if S == 0:
    result -= 1

print(result)
