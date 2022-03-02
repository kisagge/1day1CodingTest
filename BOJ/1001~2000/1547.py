# BaekJoon Onlin Judge - 1547번 공
import sys
N = int(sys.stdin.readline().rstrip())
cup = [0, 1, 0, 0]
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    cup[A], cup[B] = cup[B], cup[A]
print(cup.index(1))
