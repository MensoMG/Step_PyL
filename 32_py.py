dc = {}
for i in range(int(input())):
    a = int(input())
    
    if str(a) not in dc:
        b = f(a)
        dc[str(a)] = b
    else:
        dc[str(a)] = dc.get(str(a))
    print(dc.get(str(a)))
    a = 0
    b = 0
