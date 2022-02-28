# BaekJoon Onlin Judge - 1173번 운동
import sys
N, m, M, T, R = map(int, sys.stdin.readline().rstrip().split())
if M - m < T:
    print(-1)
else:
    totalTime = 0
    curM = m
    while N > 0:
        if curM + T <= M:
            curM += T
            N -= 1
        else:
            curM -= R
            if curM < m:
                curM = m
        totalTime += 1
    print(totalTime)