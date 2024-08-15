import sys
sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

N, R = map(int, input().split())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
pillar = branch = 0

for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))


def dfs(now, v, is_branch):
    global pillar, branch

    # 이번이 기가 노드인가?
    flag = False

    # 루트 노드가 기가 노드일 때
    if now == R and len(tree[R]) > 1:
        flag = True

    # 기둥이었는데 지금이 기가 노드일 때
    elif not is_branch and len(tree[now]) > 2:
        flag = True

    # 기둥 길이 갱신
    if flag:
        pillar = v

    for togo, tv in tree[now]:
        if not visited[togo]:
            visited[togo] = True
            if flag:
                dfs(togo, tv, flag)
            else:
                dfs(togo, v + tv, is_branch)

    # 리프 노드인데
    if len(tree[now]) == 1:
        if is_branch:
            branch = max(branch, v)
        # 아직 기둥이면
        else:
            if now != R:
                pillar = v


visited[R] = True
dfs(R, 0, False)
print(pillar, branch)
