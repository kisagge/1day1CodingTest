# BaekJoon Onlin Judge - 1269번 대칭 차집합
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A_list = list(map(int, sys.stdin.readline().rstrip().split()))
B_list = list(map(int, sys.stdin.readline().rstrip().split()))
A_list.extend(B_list)
s = list(set(A_list))
print(2* len(s) - len(A_list))
