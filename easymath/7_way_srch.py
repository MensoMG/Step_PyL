v = float(input())

if v <= 0:
    print("error")
else:
    if v <= 7.8:
        print(0)
    if 7.8 < v < 11.2:
        print(1)
    if 11.2 <= v <= 16.4:
        print(2)
    if v > 16.4:
        print(3)
