import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(4):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())

    # 안 겹칠 때
    if x2 < p1 or q2 < y1 or p2 < x1 or y2 < q1:
        print('d')

    # 점이 겹칠 때
    elif (x1 == p2 and y2 == q1) or (x1 == p2 and y1 == q2) or (x2 == p1 and y1 == q2) or (x2 == p1 and y2 == q1):
        print('c')

    # 면이 겹칠 때
    elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
        print('b')

    else:
        print('a')
        