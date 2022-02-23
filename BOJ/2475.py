# BaekJoon Onlin Judge - 2475번 검증수
lst = list(map(int, input().split()))

result = 0
for e in lst:
    result += e * e
print(result % 10)