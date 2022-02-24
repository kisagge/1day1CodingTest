# BaekJoon Onlin Judge - 1297번 TV 크기
D, H, W = map(int, input().split())
ratio = D / (H*H + W*W)**(1/2)
true_H = int(ratio * H)
true_W = int(ratio * W)
print(true_H, true_W)