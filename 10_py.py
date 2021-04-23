a = int(input())
b = int(input())
c = int(input())

cor = [a,b,c]
print(max(cor))
print(min(cor))
del cor[cor.index(max(cor))]
del cor[cor.index(min(cor))]
print(cor[0])
