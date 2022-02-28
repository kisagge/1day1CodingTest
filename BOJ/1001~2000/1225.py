# BaekJoon Onlin Judge - 1225번 이상한 곱셈
import sys
A, B = sys.stdin.readline().rstrip().split()
sumA, sumB = 0, 0
for a in A:
    sumA += int(a)
for b in B:
    sumB += int(b)
print(sumA * sumB)