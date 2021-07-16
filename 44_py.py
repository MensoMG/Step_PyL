compas = {
          'север': 0, 'юг': 0,
          'запад': 0, 'восток': 0
         }

for key, value in [input().split() for _ in range(int(input()))]:
    compas[key] += int(value)

print(compas['восток'] - compas['запад'],
      compas['север'] - compas['юг'])
