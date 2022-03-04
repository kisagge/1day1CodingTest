# BaekJoon Onlin Judge - 3004번 체스판 조각
import sys
N = int(sys.stdin.readline().rstrip())
row = N // 2 + 1
col = N - row + 2
result = row * col
print(result)