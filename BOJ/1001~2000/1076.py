# BaekJoon Onlin Judge - 1076번 저항
import sys
colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
v1 = sys.stdin.readline().rstrip()
v2 = sys.stdin.readline().rstrip()
v3 = sys.stdin.readline().rstrip()
print(int(str(colors.index(v1)) + str(colors.index(v2))) * (10**(colors.index(v3))))