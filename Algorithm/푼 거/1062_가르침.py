import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if K < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif K == 26:
    print(N)
    exit()

answer = 0
words = []
for _ in range(N):
    tmp = input()
    words.append(set(tmp[4:-4]))
learn = [False] * 26

# 기본 a, n, t, i, c는 배워야 함
for c in 'antic':
    learn[ord(c) - 97] = True


def dfs(idx, cnt):
    global answer

    if cnt == K - 5:
        possible = 0

        for word in words:
            for char in word:
                if not learn[ord(char) - 97]:
                    break
            else:
                possible += 1
        answer = max(answer, possible)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)