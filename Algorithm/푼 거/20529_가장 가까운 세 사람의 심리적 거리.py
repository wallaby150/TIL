import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    cases = list(input().split())
    answer = 10

    if N > 32:
        print(0)
        continue

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                num = 0
                for idx in range(4):
                    if cases[i][idx] != cases[j][idx]:
                        num += 1
                    if cases[j][idx] != cases[k][idx]:
                        num += 1
                    if cases[i][idx] != cases[k][idx]:
                        num += 1
                answer = min(answer, num)

    print(answer)