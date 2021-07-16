import urllib.request
import shutil

#Чтение ссылки на файл
with open(r'C:\Users\Menso_MG\Downloads\dataset_3378_2.txt', 'r') as f:
    url = f.readline()

#Открытие ссылки и запись в файл
with urllib.request.urlopen(url) as response, open('file_name.txt', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

#Чтение для посчета строк
file = open('file_name.txt', 'r')
line = file.read()

# Подсчет строк
count = 0
for i in line:
    if i == '\n':
        count += 1

#Вывод кол-ва строк
print(count)
