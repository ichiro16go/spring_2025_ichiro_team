N = int(input())
head_list = []
del_count = 0
tail = 0
for i in range(N):
  ab = list(map(int, input().split()))
  if ab[0] == 1:
    head_list.append(tail)
    tail += ab[1]
  elif ab[0] == 2:
      del_count += 1
  else:
    ans = head_list[ab[1]+del_count-1] - head_list[del_count]
    print(ans)