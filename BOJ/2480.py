# BaekJoon Onlin Judge - 2480번 주사위 세개
import sys
D1, D2, D3 = map(int, sys.stdin.readline().rstrip().split())
if D1 == D2 and D2 == D3:
    print(10000 + D1 * 1000)
elif D1 == D2:
    print(1000 + D1 * 100)
elif D2 == D3:
    print(1000 + D2 * 100)
elif D3 == D1:
    print(1000 + D3 * 100)
else:
    print(max([D1, D2, D3]) * 100)