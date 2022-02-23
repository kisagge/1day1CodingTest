# BaekJoon Onlin Judge - 1550번 16진수
hex = input()
hexAlph = ['A', 'B', 'C', 'D', 'E', 'F']
result = 0

for i in range(len(hex)):
    if hex[i] in hexAlph:
        result += (10 + hexAlph.index(hex[i])) * int(pow(16, len(hex) - i - 1))
    else:
        result += int(hex[i]) * int(pow(16, len(hex) - i - 1))
print(result)