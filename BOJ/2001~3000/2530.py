import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())
D = int(sys.stdin.readline().rstrip())
S = A * 3600 + B * 60 + C + D
H = (S // 3600) % 24
S %= 3600
M = S // 60
S %= 60
print(H, M, S)