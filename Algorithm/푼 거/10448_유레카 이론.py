answer = [0] * 1001
tri = [i * (i + 1) // 2 for i in range(1, 45)]

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000:
                answer[i + j + k] = 1
            else:
                break

T = int(input())
for _ in range(T):
    N = int(input())
    print(answer[N])