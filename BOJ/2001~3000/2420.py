# BaekJoon Onlin Judge - 2420번 사파리월드
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
result = (N - M) if N >= M else M - N
print(result)