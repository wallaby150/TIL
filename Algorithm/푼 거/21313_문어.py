N = int(input())
ans = [1, 2] * (N // 2) + ([3] if N % 2 else [])
print(*ans)
