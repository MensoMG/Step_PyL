mat, fiz, rus = [],[],[]

with open(r'C:\Users\Menso_MG\Downloads\dataset_3363_4.txt', 'r') as f:
   a = f.read().lower().split()
   ln = len(a)
  
   for i in range(ln):
      a[i] = a[i].split(';')
      print((int(a[i][1])+int(a[i][2])+int(a[i][3]))/3)
   print(a)
  
   for j in range(ln):
      mat.append(int(a[j][1]))
      fiz.append(int(a[j][2]))
      rus.append(int(a[j][3]))
   print(sum(mat)/ln,sum(fiz)/ln,sum(rus)/ln)
