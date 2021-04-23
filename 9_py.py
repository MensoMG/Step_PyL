fig = input()
figs = ["треугольник","прямоугольник","круг"]

if fig in figs[0]:
    a,b,c = int(input()),int(input()),int(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
if fig in figs[1]:
    a,b = int(input()),int(input())
    print(a*b)
if fig in figs[2]:
    r = int(input())
    print(3.14*r**2)
