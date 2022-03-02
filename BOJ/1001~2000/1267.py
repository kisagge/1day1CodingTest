# BaekJoon Onlin Judge - 1267번 핸드폰 요금
import sys
N = int(sys.stdin.readline().rstrip())
timeList = list(map(int, sys.stdin.readline().rstrip().split()))
Y, M = 0, 0
for time in timeList:
    Y += (time // 30) * 10 + 10
    M += (time // 60) * 15 + 15
if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)