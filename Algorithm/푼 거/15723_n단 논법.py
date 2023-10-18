import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a_list = [[] for _ in range(27)]  # 0번 인덱스는 사용하지 않음
count = 1

def put_relation(a, b):
    a_list[a].append(b)

for _ in range(n):
    f, b = input().split(" is ")
    a = ord(f) - ord('a') + 1
    b = ord(b) - ord('a') + 1

    put_relation(a, b)

def dfs(s, e, visited):
    if s == e:
        return True

    visited[s] = True

    for neighbor in a_list[s]:
        if not visited[neighbor]:
            if dfs(neighbor, e, visited):
                return True

    return False

m = int(input())
for _ in range(m):
    l, r = input().split(" is ")
    l = ord(l) - ord('a') + 1
    r = ord(r) - ord('a') + 1
    visited = [False] * 27
    result = "F" if not dfs(l, r, visited) else "T"
    print(result)
