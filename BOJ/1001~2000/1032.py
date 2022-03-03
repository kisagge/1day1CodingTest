# BaekJoon Onlin Judge - 1032번 명령 프롬프트
import sys
N = int(sys.stdin.readline().rstrip())
S = ''
for i in range(N):
    if S == '':
        S = list(sys.stdin.readline().rstrip())
    else:
        temp = list(sys.stdin.readline().rstrip())
        for j in range(len(S)):
            if S[j] != temp[j]:
                S[j] = '?'
print("".join(S))