import sys
sys.stdin = open("1780_종이의 개수.txt")
input = lambda: sys.stdin.readline().rstrip()

# 슬라이싱으로 풀었는데 DFS로 풀어보기

def cut(paper, size):
    start = paper[0][0]
    same = True

    # 다 같은지 확인
    for y in range(size):
        for x in range(size):
            if paper[y][x] != start:
                same = False
                break
        if not same:
            break
    else:
        # 다 같은 놈이면 카운트
        paper_count[start+1] = paper_count[start+1] + 1
        return

    # 다 같은 놈이 아니면
    cut_size = size // 3
    # y축을 기준으로 3조각으로 자르기
    for order in range(3):
        first = []
        second = []
        third = []
        for i in range(cut_size):
            line = paper[i + (order * cut_size)]
            first.append(line[0:cut_size])
            second.append(line[cut_size:cut_size*2])
            third.append(line[cut_size*2:cut_size*3])
        cut(first, cut_size)
        cut(second, cut_size)
        cut(third, cut_size)


N = int(input())
whole_paper = list(list(map(int, input().split())) for _ in range(N))
paper_count = [0, 0, 0]     # -1, 0, 1
cut(whole_paper, N)
for count in paper_count:
    print(count)

'''
10
12
11
'''
