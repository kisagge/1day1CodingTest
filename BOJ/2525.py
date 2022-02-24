# BaekJoon Onlin Judge - 2525번 오븐시계
import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())
M = A * 60 + B + C
H = (M // 60) % 24
M %= 60
print(H, M)
