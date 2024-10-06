from collections import deque

N = int(input())  # 카드 갯수
nums = list(map(int, input().split()))  # 카드에 적힌 숫자들

# deque에 (숫자, 인덱스) 쌍으로 저장
dq = deque((num, i + 1) for i, num in enumerate(nums))
result = []

while dq:
    num, index = dq.popleft()  # 첫 번째 요소 꺼내기
    result.append(index)  # 결과에 인덱스 추가

    if num > 0:
        dq.rotate(-(num - 1))  # 오른쪽으로 회전
    else:
        dq.rotate(-num)  # 왼쪽으로 회전

# 결과 출력
print(' '.join(map(str, result)))