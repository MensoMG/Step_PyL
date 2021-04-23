a = []
while True:
    s = int(input())
    a.append(s)
    if 0 in a:
        print(sum(a))
        break
