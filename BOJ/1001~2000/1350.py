# BaekJoon Onlin Judge - 1350번 진짜 공간
import sys
N = int(sys.stdin.readline().rstrip())
filesList = list(map(int, sys.stdin.readline().rstrip().split()))
disc = int(sys.stdin.readline().rstrip())
totalDisc = 0
for f in filesList:
    if f <= disc:
        if f != 0:
            totalDisc += disc
    else:
        if f%disc == 0:
            totalDisc += disc * (f // disc)
        else:
            totalDisc += disc * (f // disc + 1)
print(totalDisc)
