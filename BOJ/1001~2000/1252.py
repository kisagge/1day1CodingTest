# BaekJoon Onlin Judge - 1252번 이진수 덧셈
import sys
A, B = sys.stdin.readline().rstrip().split()
A = '0b' + A
B = '0b' + B
result = int(A, 2) + int(B, 2)
print('{0:b}'.format(result))