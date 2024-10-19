N = int(input())
nums = map(int, input().split())
T, P = map(int, input().split())

print(sum(num // T + bool(num % T) for num in nums))
print(N // P, N % P)
