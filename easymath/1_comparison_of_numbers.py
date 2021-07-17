print("Для сравнения двух чисел-")
print("-введите их в консоли-")
print("-вводя их поочередо-")
a = int(input())
b = int(input())

if a < b:
    print("Первое меньше второго")
elif a > b:
    print("Второе большое первого")
else:
    if a == b:
        print("Числа равны")
