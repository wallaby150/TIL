K = int(input())
text = input()
rows = len(text) // K

table = []
for i in range(rows):
    segment = text[i * K:(i + 1) * K]
    if i % 2 == 1:
        segment = segment[::-1]
    table.append(segment)

ans = []
for col in range(K):
    for row in range(rows):
        ans.append(table[row][col])
print("".join(ans))
