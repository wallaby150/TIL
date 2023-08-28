import sys
sys.stdin = open("2630_색종이 만들기.txt")
input = lambda: sys.stdin.readline().rstrip()


def cut(p, l):
    cut_size = l // 2
    upper_left = []
    upper_right = []
    under_left = []
    under_right = []
    for row in p[:cut_size]:
        upper_left.append(row[:cut_size])
        upper_right.append(row[cut_size:])
    for row in p[cut_size:]:
        under_left.append(row[:cut_size])
        under_right.append(row[cut_size:])

    solve(upper_left)
    solve(upper_right)
    solve(under_left)
    solve(under_right)


def solve(paper):
    global white, blue

    start_color = paper[0][0]
    length = len(paper)
    same = True
    for y in range(length):
        for x in range(length):
            if paper[y][x] != start_color:
                same = False

    # 잘려진 종이의 색깔이 통일되어 있으면
    if same == True:
        if start_color == 1:
            blue += 1
        else:
            white += 1
    else:
        cut(paper, length)


N = int(input())
whole_paper = list(list(map(int, input().split())) for _ in range(N))
white = 0
blue = 0
solve(whole_paper)
print(white)
print(blue)

'''
9
7
'''