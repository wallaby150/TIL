import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

def pre(n):
    answer = n
    l, r = tree[n]
    if l != '.':
        answer += pre(l)
    if r != '.':
        answer += pre(r)
    return answer


def inorder(n):
    answer = ''
    l, r = tree[n]
    if l != '.':
        answer += inorder(l)
    answer += n
    if r != '.':
        answer += inorder(r)
    return answer

def post(n):
    answer = ''
    l, r = tree[n]
    if l != '.':
        answer += post(l)
    if r != '.':
        answer += post(r)
    answer += n
    return answer


print(pre('A'))
print(inorder('A'))
print(post('A'))
