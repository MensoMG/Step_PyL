a,b=set(),set()
for i in range(int(input())): a.add(input().lower())
for i in range(int(input())):
    for j in input().lower().split(): b.add(j)
for i in b-a: print(i)
