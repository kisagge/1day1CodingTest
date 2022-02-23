# BaekJoon Onlin Judge - 2845번 파티가 끝나고 난 뒤
L, P = map(int, input().split())
part = list(map(int, input().split()))

true_part = L * P
for p in part:
    print(p - true_part, end=" ")