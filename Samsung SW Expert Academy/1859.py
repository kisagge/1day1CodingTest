# Samsung SW Expert Academy 1859 - 백만 장자 프로젝트
TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]
    margin = 0
    maxVal = lst[0]
    for i in range(1, N):
        if maxVal > lst[i]:
            margin += maxVal - lst[i]
        else:
            maxVal = lst[i]
    print("#%s"%tc, margin)