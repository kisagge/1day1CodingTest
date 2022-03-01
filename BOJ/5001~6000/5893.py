# BaekJoon Onlin Judge - 5893번 17배
import sys
A = '0b' + sys.stdin.readline().rstrip()
result = int(A, 2) * 17
print('{0:b}'.format(result))