import sys
input = lambda : sys.stdin.readline().rstrip()

d, p = map(int, input().split())
pipes = [list(map(int, input().split())) for _ in range(p)]

# 파이프를 용량(Ci) 기준으로 내림차순 정렬
pipes.sort(key=lambda x: -x[1])


def find_max_capacity():
    possible_lengths = set()  # 만들 수 있는 길이들을 저장할 집합

    for length, capacity in pipes:
        # 만약 현재 파이프의 길이만으로 D를 만들 수 있으면, 바로 그 용량을 반환
        if length == d:
            return capacity

        new_lengths = set()  # 새로운 길이 조합을 저장할 임시 집합

        # 현재까지 가능한 모든 길이에 이 파이프의 길이를 더해봄
        for existing_length in possible_lengths:
            new_length = existing_length + length

            # 새로운 길이가 D가 되면 현재 파이프의 용량을 반환
            if new_length == d:
                return capacity

            # 새로운 길이가 D보다 작으면 새로운 길이 조합에 추가
            if new_length < d:
                new_lengths.add(new_length)

        # 현재 파이프의 길이도 새로운 길이 조합에 추가
        new_lengths.add(length)

        # 가능한 길이 집합에 새로운 길이 조합들을 추가
        possible_lengths.update(new_lengths)

    return 0  # 입력 보장이 없다면 실행될 라인


print(find_max_capacity())