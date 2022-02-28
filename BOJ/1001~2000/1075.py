# BaekJoon Onlin Judge - 1075번 나누기
import sys
N = sys.stdin.readline().rstrip()
F = int(sys.stdin.readline().rstrip())
newN = int(N[:len(N)-2] + '00')
if newN%F != 0:
    newN += F - newN%F
print(str(newN)[len(str(newN))-2:])
