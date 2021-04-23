a,b,c,d = int(input()),int(input()),int(input()),int(input())

s = ''
# формируем шапку таблицы
for i in range (c, d + 1):
    s += '\t%s' % i
    
# заполняем строки таблицы
for i in range(a, b + 1):
    s += '\n%s' % i # выводим текущее число из умножаемого столбеца
    for j in range (c, d + 1):
        s += '\t%s' % (i * j) # выводим результат умножения соответствующих чисел

print(s)
