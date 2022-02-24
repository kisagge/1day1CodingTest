# BaekJoon Onlin Judge - 2752번 세수정렬
import sys
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
num_list.sort()
for num in num_list:
    print(num, end=" ")