mx = 0

with open(r'C:\Users\Menso_MG\Downloads\dataset_3363_3.txt', 'r') as f:
   a = f.read().lower().split()

   for i in range(len(a)):
      cnt = 0
      for j in range(len(a)):
         if a[i] == a[j]:
            cnt += 1
      if cnt > mx:
         mx = cnt
         mxw = a[i]

print(mxw,mx)
