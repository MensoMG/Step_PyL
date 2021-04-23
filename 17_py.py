a,b = int(input()),int(input())
s=[]
allo=0
for i in range(a,b+1):
    if i % 3 == 0:
        s.append(i)
        allo+=1
print(sum(s)/allo)
