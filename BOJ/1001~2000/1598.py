# BaekJoon Onlin Judge - 1598번 꼬리를 무는 숫자 나열
import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
Ax, Ay, Bx, By = (A-1) // 4, (A-1) % 4, (B-1) // 4, (B-1) % 4
print(max(Bx, Ax) - min(Bx, Ax) + max(By, Ay) - min(By, Ay))
