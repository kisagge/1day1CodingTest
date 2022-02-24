# BaekJoon Onlin Judge - 1011번 Fly me to the Alpha Centauri
TC = int(input())
for i in range(0, TC):
  x, y = map(int, input().split())
  k = y - x
  n = 1
  l = 0
  t = 1
  while (1):
    if k <= l + 2*n:
      if k > l + n:
        t += 1
      break
    l += 2*n
    n += 1
    t += 2
  
  print(t)