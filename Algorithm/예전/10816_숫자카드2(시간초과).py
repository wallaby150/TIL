N = int(input())    # 가지고 있는 카드의 수
cards = list(map(int, input().split()))
M = int(input())    # 확인해볼 숫자의 갯수
check_list = list(map(int, input().split()))

for num in check_list:
    print(cards.count(num), end=" ")
    
    
# 시간초과 나버림