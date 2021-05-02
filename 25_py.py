lst= [int(i) for i in input().split()]
op = int(input())

if op not in lst:
    print("Отсутствует")
x = [i for i, ltr in enumerate(lst) if ltr == op]
for i in range(len(x)):
    print(x[i],end=" ")
