# put your python code here
from math import sqrt
a = float(input())
h = float(input())
if h <= 0 or a <=0:
    print("error")
else:
    V = ((a**2 * h)/(4*sqrt(3)))
    S = ((a**2 * sqrt(3)) / 4 + (3*a)/2 * sqrt(h**2 + (a**2 / 12)))
    num = float('{:.3f}'.format(V))
    num1 = float('{:.3f}'.format(S))
    print(num, num1)
