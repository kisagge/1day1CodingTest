# BaekJoon Onlin Judge - 1712번 손익분기점
import sys
A, B, C = map(int, sys.stdin.readline().split())
if B >= C:
  print(-1)
else:
  ans = A // (C - B) + 1
  print("%d"%ans)