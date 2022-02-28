# BaekJoon Onlin Judge - 1100번 하얀 칸
import sys
ans = 0
for i in range(8):
    K = sys.stdin.readline().rstrip()
    if i%2 == 0:
        for j in range(0, 8, 2):
            if K[j] == "F":
                ans += 1
    else:
        for j in range(1, 8, 2):
            if K[j] == "F":
                ans += 1
print(ans)