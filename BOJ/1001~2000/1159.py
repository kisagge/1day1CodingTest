# BaekJoon Onlin Judge - 1159번 농구 경기
import sys
alp = [0] * 26
ans = ''
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    name = sys.stdin.readline().rstrip()
    alp[ord(name[0]) - 97] += 1

for i in range(len(alp)):
    if alp[i] >= 5:
        ans += chr(97 + i)

if ans == '':
    ans += 'PREDAJA'
print(ans)
    
        