# BaekJoon Onlin Judge - 1977번 완전제곱수
import sys
X = int(sys.stdin.readline().rstrip())
Y = int(sys.stdin.readline().rstrip())
lst = [x * x for x in range(1, 101) if X <= x * x <= Y]
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)