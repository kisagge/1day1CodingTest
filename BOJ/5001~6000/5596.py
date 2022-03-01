# BaekJoon Onlin Judge - 5596번 시험 점수
import sys
s_list = list(map(int, sys.stdin.readline().rstrip().split()))
t_list = list(map(int, sys.stdin.readline().rstrip().split()))
print(max(sum(s_list), sum(t_list)))
