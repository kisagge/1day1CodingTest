# BaekJoon Onlin Judge - 1037번 약수
import sys
num = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
num_list.sort()
if num%2 == 1:
    print(num_list[num//2] ** 2)
else:
    print(num_list[0] * num_list[num - 1])