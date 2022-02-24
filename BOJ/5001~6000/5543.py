# BaekJoon Onlin Judge - 5543번 상근날드
import sys
menu_list = []
for i in range(5):
    menu_list.append(int(input()))
print(min(menu_list[:3]) + min(menu_list[3:5]) - 50)