import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
course = [0] + list(map(int, input().split()))
turn = sum(course)
tmp = 0

if K == turn:
    print(N)

elif K < turn:
    for i in range(1, N):
        tmp += course[i]
        if tmp > K:
            print(i)
            break

# 반환점보다 길면 역순으로 빼준다.
else:
    K -= turn
    for j in range(N, 0, -1):
        tmp += course[j]
        if tmp > K:
            print(j)
            break
