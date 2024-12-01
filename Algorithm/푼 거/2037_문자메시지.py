def calculate_typing_time(p, w, text):
    keyboard = [
        [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], 
        ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], 
        ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
    ]

    total_time = 0
    previous_key = None

    for char in text:
        if char == ' ':
            total_time += p
            previous_key = None
            continue

        for key_index, key_chars in enumerate(keyboard):
            if char in key_chars:
                char_position = key_chars.index(char)
                if key_index == previous_key:
                    total_time += w
                total_time += (char_position + 1) * p
                previous_key = key_index
                break

    return total_time


p, w = map(int, input().split())
text = input().strip()
print(calculate_typing_time(p, w, text))