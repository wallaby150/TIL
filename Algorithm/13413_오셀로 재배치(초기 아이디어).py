import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    now = list(input())
    target = list(input())
    cnt = 0


    while now != target:
        # 둘의 글자수는 같고 위치만 다르면
        if target.count("W") == now.count("W"):
            for j in range(N):
                if target[j] != now[j]:
                    char = target[j]

                    for k in range(j, N):
                        if now[k] == char and now[k] != target[k]:
                            now[j] = target[j]
                            now[k] = target[k]
                            cnt += 1

        else:
            for i in range(N):
                if target[i] != now[i]:
                    now[i] = target[i]
                    cnt += 1
                    break

    print(cnt)