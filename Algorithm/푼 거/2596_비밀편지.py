import sys
input = lambda: sys.stdin.readline().rstrip()

code_map = {
    "000000": "A", "001111": "B", "010011": "C", "011100": "D",
    "100110": "E", "101001": "F", "110101": "G", "111010": "H"
}

N = int(input())
text = input()

decoded = []
for i in range(N):
    segment = text[i * 6:(i + 1) * 6]
    if segment in code_map:
        decoded.append(code_map[segment])
    else:
        # 하나만 다른 경우 찾기
        found = False
        for key in code_map:
            diff = sum(1 for a, b in zip(segment, key) if a != b)
            if diff == 1:  # 하나만 다르면 유효한 문자로 해석
                decoded.append(code_map[key])
                found = True
                break
        if not found:  # 오류 발생 위치 출력 후 종료
            print(i + 1)
            sys.exit()

print("".join(decoded))
