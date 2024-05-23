N = int(input())
nums = sorted(list(map(int, input().split())))
cnt = 0


def binary_search(idx):
    num = nums[idx] / 0.9
    l, r = idx + 1, N - 1
    while l <= r:
        mid = (l + r) // 2
        # 찾고자 하는 값보다 작다면
        if nums[mid] <= num:
            l = mid + 1
        # 찾고자 하는 값보다 크다면
        elif nums[mid] > num:
            r = mid - 1
    return r


for i in range(N-1):
    j = binary_search(i)
    cnt += max(0, j-i)

print(cnt)
