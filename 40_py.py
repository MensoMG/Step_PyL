import requests

s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
cn = 0

while True:
    if not s.text.startswith('We'):
        s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s.text)
        cn += 1
        print(str(cn)+ ' file check, ', 'name '+ s.text)
    else:
        print(s.text)
        break
