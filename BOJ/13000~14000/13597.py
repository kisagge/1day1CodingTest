# BaekJoon Onlin Judge - 13597번 Tri-du
import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
result = A if A >= B else B
print(result)