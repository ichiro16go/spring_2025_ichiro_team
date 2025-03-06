N = input()
S = list(input())
T = list(input())

if S==T:
  print('Yes')
  exit()

if abs(len(S)-len(T)) > 1:
  print('No')
  exit()

if len(S) == len(T):
  count = 0
  for i in range(len(S)):
    if S[i] != T[i]:
      count += 1
      if count > 1:
        print('No')
        exit()
  print('Yes')
  exit()      
  
if abs(len(S) - len(T)) == 1:
  count = 0
  for i in range(max(len(S), len(T))):
    if i == max(len(S), len(T))-1 and len(T) != len(S):
      if count <= 1:
        print('Yes')
        exit()
    if S[i] != T[i]:
      if len(S) < len(T):
        S.insert(i,T[i])
      else:
        T.insert(i, S[i])
      count += 1
      if count > 1:
        print('No')
        exit()
  if count == 1:
    print('Yes')
    exit()

print('No')