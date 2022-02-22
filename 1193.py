# BaekJoon Onlin Judge - 1193번 분수찾기
lst = []
for i in range(1,4500):
    lst.append(i * (i+1) // 2)

idx = 0
j = lst[idx]
targetNum = int(input())
while targetNum > j:
    idx += 1
    j = lst[idx]

if idx == 0:
    print('1/1')
else:
    son = 1
    mom = idx + 1
    for i in range(lst[idx - 1] + 1, targetNum):
        son += 1
        mom -= 1
    if idx%2 == 0:
        son, mom = mom, son
    print('{0}/{1}'.format(son, mom))