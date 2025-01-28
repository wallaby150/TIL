text = input()

high, low = "", ""
m_count = 0

for char in text:
    if char == 'M':
        m_count += 1
    elif char == 'K':
        high += '5' + '0' * m_count
        low += '1' + '0' * (m_count - 1) + '5' if m_count else '5'
        m_count = 0

if m_count:
    high += '1' * m_count
    low += '1' + '0' * (m_count - 1)

print(high)
print(low)
