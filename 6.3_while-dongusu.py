x = 0
while x <= 100: 
    print(x)
    x += 1

name = ''
while not name.strip():
    #kullanıcı boşluk girerse strip ile baş ve sondan boşlukları siler ve tekrar isim girilmesini ister
    name  = input('İsminzi giriniz: ')

print (f'Merhaba {name}')