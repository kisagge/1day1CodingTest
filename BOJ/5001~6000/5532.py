# BaekJoon Onlin Judge - 5532번 방학 숙제
import sys
L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
korean = (A//C) if A%C == 0 else (A//C + 1)
mathmatics = (B//D) if B%D == 0 else (B//D + 1)
print(L - max(korean, mathmatics))