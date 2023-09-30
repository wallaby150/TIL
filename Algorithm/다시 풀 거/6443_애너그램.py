import sys
input = lambda : sys.stdin.readline().rstrip()

def solve(index, w):
    if index == length:
        print(w)
        return

    else:
        for i in range(length):
            if visited[i]:
                tmp = w + word[i]
                if tmp not in ans:
                    visited[i] = False
                    ans.add(tmp)
                    solve(index + 1, tmp)
                    visited[i] = True


N = int(input())
for _ in range(N):
    word = sorted(list(input()))
    ans = set()
    length = len(word)
    visited = [True] * length
    solve(0, "")