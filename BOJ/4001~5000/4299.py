# BaekJoon Onlin Judge - 4299번 AFC 윔블던
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
if a < b:
    print(-1)
else:
    result_sum = (a + b) / 2
    result_minus = abs((a - b) / 2)
    if result_sum.is_integer() and result_minus.is_integer():
        print(int(result_sum), int(result_minus))
    else:
        print(-1)