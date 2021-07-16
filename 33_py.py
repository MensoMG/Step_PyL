import re

with open(r'C:\Users\Menso_MG\Downloads\dataset_3363_2.txt', 'r') as f:
   a = f.readline()
   print(re.sub('([A-Za-z])(\d+)', lambda x: x.group(1) * int(x.group(2)), a))
