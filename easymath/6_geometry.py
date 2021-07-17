# подключаю модуль math и импортирую из него все нужные функции
from math import sqrt, exp, sin, log, cos, asin, sqrt, pi
x = -2.3 #пример значения
y = 8.72 #пример значения
# вычислить выражение, результат занести в переменную z        
z2=1.2 * sqrt(2-cos(y)**2)
z1=asin(cos(x+(sqrt(3)/2)*pi))
z = (z1+z2)/(x**2+y**2+1)
print(round(z, 5))
