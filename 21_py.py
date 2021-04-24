s = [int(i) for i in input().split()]
suml = []
l = -1
r = -len(s)+1
c = 0
if len(s) == 1:
  print(s[0])
else: 
  for i in range(len(s)):
    suml.append(s[l]+s[r]) 
    l += 1 
    r += 1 
    c += 1 
  print(" ".join(list(map(str, suml))))
