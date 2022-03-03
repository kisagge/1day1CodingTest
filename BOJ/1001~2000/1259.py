# BaekJoon Onlin Judge - 1259번 팰린드롬수
import sys
def pellindrom(S):
    for i in range(len(S)//2):
        if S[i] != S[len(S) - 1 - i]:
            return False
    return True

while True:
    S = list(sys.stdin.readline().rstrip())
    if S[0] == '0':
        break
    if pellindrom(S):
        print('yes')
    else:
        print('no')