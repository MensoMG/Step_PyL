s = [int(i) for i in input().split()]
res = [x for x in set(s) if s.count(x) > 1]
for elem in res:
    print(elem, end=' ')
