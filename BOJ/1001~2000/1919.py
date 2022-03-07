# BaekJoon Onlin Judge - 1919번 애너그램 만들기
import sys
a_alpha = [0] * 26
b_alpha = [0] * 26
answer = 0

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

for e in a:
    a_alpha[ord(e) - 97] += 1
for e in b:
    b_alpha[ord(e) - 97] += 1

for i in range(26):
    if a_alpha[i] != b_alpha[i]:
        answer += abs(a_alpha[i] - b_alpha[i])
        
print(answer)