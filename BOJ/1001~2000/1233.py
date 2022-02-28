import sys
S1, S2, S3 = map(int, sys.stdin.readline().rstrip().split())
ans = [0] * (S1 * S2 * S3 + 1)
for a in range(1, S1+1):
    for b in range(1, S2+1):
        for c in range(1, S3+1):
            ans[a+b+c] += 1
print(ans.index(max(ans)))
