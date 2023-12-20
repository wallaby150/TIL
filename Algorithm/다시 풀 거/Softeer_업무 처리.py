import sys
input = sys.stdin.readline
from collections import deque

# 높이 H, 업무 K, 작업일수 R
H, K, R = map(int, input().split())
memberNum = 2 ** (H+1)
notLeaf = 2 ** H - 1
tree = [deque() for _ in range(memberNum)]
for i in range(2**H):
    tree[2**H + i] = deque(map(int, input().split()))
answer = 0

for day in range(R):
    for t in range(1, notLeaf + 1):
        if t == 1:
            if tree[t]:
               answer += tree[t].popleft()

        # 홀수라면
        if day % 2:
            if tree[t*2]:
                tree[t].append(tree[t*2].popleft())
        else:
            if tree[t*2+1]:
                tree[t].append(tree[t*2+1].popleft())

print(answer)

# https://acg6138.tistory.com/24 참고