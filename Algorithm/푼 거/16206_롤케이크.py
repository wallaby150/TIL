N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

nums.sort(key=lambda x: (x % 10, x))
for num in nums:
    if num == 10:
        ans += 1
    else:
        if not M:
            break

        # 10단위 숫자에 자를 수 있는 횟수가 넉넉하면
        if num % 10 == 0 and M >= (num // 10 - 1):
            ans += num // 10
            M -= num // 10 - 1

        else:
            ans += min(M, num // 10)
            M -= min(M, num // 10)

print(ans)
