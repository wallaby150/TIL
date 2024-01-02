N = int(input())    # 가지고 있는 카드의 수
cards = sorted(list(map(int, input().split())))     # 가지고 있는 카드를 렬해서 리스트에 저장한다.
M = int(input())    # 확인해볼 숫자의 갯수
check_list = list(map(int, input().split()))        # 확인해볼 숫자 리스트

count_list = list([0] * (cards[-1] - cards[0] + 1))     # 카운팅 정렬할 배열. 크기는 최소값~최대값의 차이만큼

for card in cards:
    count_list[card-cards[0]] += 1                  # 최소값을 0으로 만들어서 해당 인덱스에 카운팅

for num in check_list
    if cards[0] <= num <= cards[-1]:                # 확인해볼 값이 카운팅 리스트에 없으면 통과
        print(count_list[num-cards[0]], end=" ")
    else:
        print(0, end=" ")
