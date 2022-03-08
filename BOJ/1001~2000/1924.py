# BaekJoon Onlin Judge - 1402번 아무래도이문제는A번난이도인것같다
import sys
M, D = map(int, sys.stdin.readline().rstrip().split())
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day365 = D
if M == 2:
    day365 += 31
elif M == 3:
    day365 += 59
elif M == 4:
    day365 += 90
elif M == 5:
    day365 += 120
elif M == 6:
    day365 += 151
elif M == 7:
    day365 += 181
elif M == 8:
    day365 += 212
elif M == 9:
    day365 += 243
elif M == 10:
    day365 += 273
elif M == 11:
    day365 += 304
elif M == 12:
    day365 += 334

print(days[day365 % 7])