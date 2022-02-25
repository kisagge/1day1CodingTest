# BaekJoon Onlin Judge - 1018번 체스판 다시 칠하기
import sys
def seperateString(s1, s2):
    cnt = 0
    for a, b in zip(s1, s2):
        if a != b:
            cnt += 1
    return cnt

WB = 'WBWBWBWB'
BW = 'BWBWBWBW'
chess = []

case1 = [WB, BW, WB, BW, WB, BW, WB, BW]
case2 = [BW, WB, BW, WB, BW, WB, BW, WB]

def chessPlane(I, J, sep):
    temp = 0
    for i in range(0, 8):
        temp += seperateString(chess[I+i][J:J+8], sep[i])
    return temp
             
H, W = map(int, sys.stdin.readline().rstrip().split())

for i in range(H):
    chess.append(sys.stdin.readline().rstrip())

minPaint = 9999
for i in range(0, H - 7):
    for j in range(0, W - 7):
        minPaint = min(minPaint, chessPlane(i, j, case1))
        minPaint = min(minPaint, chessPlane(i, j, case2))
        
print(minPaint)