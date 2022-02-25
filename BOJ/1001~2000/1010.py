# BaekJoon Onlin Judge - 1010번 다리 놓기
import sys
def multipleRange(From, To):
    result = 1
    for i in range(From, From - To, -1):
        result *= i
    return result

TC = int(sys.stdin.readline().rstrip())
for tc in range(TC):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print(multipleRange(M, N) // multipleRange(N, N-1))
