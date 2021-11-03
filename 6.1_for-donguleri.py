numbers = [1, 2, 3, 4, 5]

for num in numbers:
    # for + degisken adi + in + liste adı
    print(num)
    # liste içerisindeki her değişkeni num içine at ve ekrana yazdır

names = ['ali', 'veli', 'kemal']

for a in names:
    print(f'Benim adım {a}')

name = 'Ayse Erdanisman'
for b in name:
    print(b)

d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

f = {'k1':1, 'k2':2, 'k3':3}
for item in f.items():
    print(item)

g = {'k1':1, 'k2':2, 'k3':3}
for key,value in g.items():
    print(value) #or key