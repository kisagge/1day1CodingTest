# BaekJoon Onlin Judge - 1110번 더하기 사이클
import sys
count = 0
N = int(sys.stdin.readline())
l = N
target = 0
while True:
  count += 1
  if N == 0:
    print("1")
    break
  A, B = N//10, N%10
  C = A+B
  N = B*10 + C%10
  if N == l:
    print("%d"%count)
    break