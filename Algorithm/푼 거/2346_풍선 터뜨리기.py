import sys
sys.stdin = open("../input.txt")
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) # 카드 갯수
nums = list(map(int, input().split())) # 카드에 적힌 숫자들
order = list(range(N))  # 카드 순서들
idx = 1 # 지금 순서
move = 0 # 움직일 위치

while nums:
    if move >= 0:
        idx = (idx + move - 1) % len(nums)
    else:
        idx = (idx + move) % len(nums)

    print(order.pop(idx) + 1, end=' ')
    move = nums.pop(idx)