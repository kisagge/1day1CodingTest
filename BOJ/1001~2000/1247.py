# BaekJoon Onlin Judge - 1247번 부호
import sys
for i in range(3):
    N = int(sys.stdin.readline().rstrip())
    S = 0
    for j in range(N):
        S += int(sys.stdin.readline().rstrip())
    if S > 0:
        print('+')
    elif S < 0:
        print('-')
    else:
        print('0')