N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))

count = 0

for i in range(N):
    count += A[i] * B[i]

print(count)