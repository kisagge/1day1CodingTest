# BaekJoon Onlin Judge - 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰
cur_chess = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)):
    print(chess[i] - cur_chess[i], end=" ")