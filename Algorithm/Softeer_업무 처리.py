import sys
sys.stdin = open("Softeer_업무 처리.txt")
input = sys.stdin.readline


def solve():
    # 조직의 높이, 말단에 대기하는 업무의 개수, 진행되는 날짜 수
    H, K, R = map(int, input().split())
    print(H, K, R)

    for _ in range(H*2):
        task = list(map(int, input().split()))
        print(task)



    ans = 0
    return ans


for tc in range(2):
    print(f'#{tc+1} : {solve()}')