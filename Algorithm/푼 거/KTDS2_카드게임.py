import sys
sys.stdin = open("KTDS2_카드게임.txt")


def discard(cards, opposite, k):
    # if k 있을 때 없을 때
    if cards[0] + k in cards:
        for idx in range(len(cards)):
            if cards[idx] > cards[0] + k:
                return idx
        else:
            return len(cards)
    else:
        for idx in range(len(cards)):
            if opposite:
                if cards[idx] > opposite[0]:
                    return idx
        else:
            return len(cards)


def solution(cards1, cards2, k):
    cards1.sort()
    cards2.sort()
    all_cards = cards1 + cards2
    all_cards.sort()
    count = 0

    # turn이 False면 cards1, True면 cards2
    if all_cards[0] in cards1:
        turn = False
    else:
        turn = True

    while len(all_cards) != 0:
        if turn == False:
            i = discard(cards1, cards2, k)
            all_cards = all_cards[i:]
            cards1 = cards1[i:]
        else:
            i = discard(cards2, cards1, k)
            all_cards = all_cards[i:]
            cards2 = cards2[i:]

        turn = not turn
        count += 1

    return count


for tc in range(int(input())):
    cards1 = list(map(int, input().split()))
    cards2 = list(map(int, input().split()))
    k = int(input())

    print(solution(cards1, cards2, k))

'''
대충 cards1, cards2와 k를 주고
오름차순으로 카드를 버려야 하는데, 최소 턴을 구하라는 것.
특별한 것은 k를 준다. 이것은 버린 카드보다 k만큼 적으면 (마지막 숫자-k) 카드를 뒤에 버릴 수 있다.
그러므로 한 턴에 min(cards1) ~ card-k까지 버릴 수 있어서 이득.

결론 : 인덱싱도 잘못 하고, discard의 for문에 else를 잘못 잡음.
내 머릿속에 논리가 부족했다. 디버깅 툴은 내 실력이 아니다.
'''

'''
2
6
2
'''