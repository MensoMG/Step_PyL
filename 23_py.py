s = []
summ = []
while True:
    s.append(int(input()))
    if sum(s) == 0:
        for i in s:
            summ.append(i**2)
        print(sum(summ))
        break
