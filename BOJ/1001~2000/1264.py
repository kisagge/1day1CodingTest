# BaekJoon Onlin Judge - 1264번 모음의 개수
import sys
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
while True:
    S = sys.stdin.readline().rstrip()
    if S == '#':
         break
    cnt = 0
    for s in S:
        if s in vowels:
            cnt += 1
    print(cnt)