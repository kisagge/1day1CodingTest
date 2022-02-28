# BaekJoon Onlin Judge - 1813번 논리학 교수
import sys
N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst.sort()
ans = 0
for e in lst:
    if e == lst.count(e):
        ans = e
if 0 in lst and ans == 0:
    ans = -1
print(ans)