# BaekJoon Onlin Judge - 1284번 집 주소
import sys
while True:
    N = sys.stdin.readline().rstrip()
    k = 0
    if N == '0':
        break
    for n in N:
        if n == '0':
            k += 5
        elif n == '1':
            k += 3
        else:
            k += 4
    print(k + 1)