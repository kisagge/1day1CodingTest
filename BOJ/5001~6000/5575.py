import sys
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(map(int, sys.stdin.readline().rstrip().split()))
A_Time = A[3] * 3600 + A[4] * 60 + A[5] - (A[0] * 3600 + A[1] * 60 + A[2])
B_Time = B[3] * 3600 + B[4] * 60 + B[5] - (B[0] * 3600 + B[1] * 60 + B[2])
C_Time = C[3] * 3600 + C[4] * 60 + C[5] - (C[0] * 3600 + C[1] * 60 + C[2])
A_H = A_Time // 3600
A_Time %= 3600
A_M = A_Time // 60
A_Time %= 60
B_H = B_Time // 3600
B_Time %= 3600
B_M = B_Time // 60
B_Time %= 60
C_H = C_Time // 3600
C_Time %= 3600
C_M = C_Time // 60
C_Time %= 60
print(A_H, A_M, A_Time)
print(B_H, B_M, B_Time)
print(C_H, C_M, C_Time)