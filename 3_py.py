X = int (input())
H = int (input())
M = int (input())

print(H+(X//60)+(M+(X%60))//60)
print((M+(X%60))%60)
