# BaekJoon Onlin Judge - 1568번 새
import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0
num = 1
while N > 0:
    if num <= N:
        N -= num
    else:
        num = 1
        N -= num
    num += 1
    cnt += 1
print(cnt)