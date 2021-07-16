k_crypt = dict(zip(input(), input()))
d_kv = []

def decode_k(dec_k):     #Функция дешифровки по ключу
    for i in dec_k:
        d_kv.append(k_crypt.get(i))
    return (''.join(d_kv))


def decode_v(dec_v):     #Функция дешифровки по значению ключа
    d_kv = []
    inv_map = {v: k for k, v in k_crypt.items()} #Инверсия ключей и значений
    for j in dec_v:
        d_kv.append(inv_map.get(j))
    return (''.join(d_kv))
    
    
print(decode_k(input()),'\n',decode_v(input()),sep='')
