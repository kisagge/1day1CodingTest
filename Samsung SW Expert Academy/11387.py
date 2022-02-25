# Samsung SW Expert Academy - 11387 몬스터 사냥
TC = int(input()) 
for tc in range(1, TC+1): 
    D, L, N = map(int, input().split()) 
    print("#%d %d"%(tc, (N*D + D*L*N*(N-1) / 200)))
