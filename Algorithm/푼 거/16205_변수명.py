def convert_to_cases(t, s):
    if t == 1:  # camelCase
        words = []
        current = ""
        for char in s:
            if char.isupper():
                if current:
                    words.append(current)
                current = char.lower()
            else:
                current += char
        words.append(current)
    elif t == 2:  # snake_case
        words = s.split('_')
    elif t == 3:  # PascalCase
        words = []
        current = ""
        for char in s:
            if char.isupper():
                if current:
                    words.append(current)
                current = char.lower()
            else:
                current += char
        words.append(current)

    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    snake_case = '_'.join(words).lower()
    pascal_case = ''.join(word.capitalize() for word in words)

    return camel_case, snake_case, pascal_case


type, text = input().split()
type = int(type)

camel, snake, pascal = convert_to_cases(type, text)
print(camel)
print(snake)
print(pascal)
