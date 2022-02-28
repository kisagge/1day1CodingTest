# BaekJoon Onlin Judge - 1362번 펫
import sys
cnt = 1
while True:
    O, W = map(int, sys.stdin.readline().rstrip().split())
    if O == 0:
        break
    isDead = False
    while True:
        cmds, n = sys.stdin.readline().rstrip().split()
        if cmds == 'E' and isDead is not True:
            W -= int(n)
            if W <= 0:
                isDead = True
        elif cmds == 'F' and isDead is not True:
            W += int(n)
        elif cmds == '#':
            if isDead:
                print(cnt, 'RIP')
            else:
                if W > O / 2 and W < 2 * O:
                    print(cnt, ':-)')
                else:
                    print(cnt, ':-(')
            cnt += 1
            break