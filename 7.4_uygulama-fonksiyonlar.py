# 1- Göderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaznız.
sayac = 0
def yaz(kelime, adet):
    print(kelime * adet)
yaz('Merhaba\n', 10)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız
def listeOlustur(*params):
    liste = []

    for param in params:
        liste.append(param)

    return liste

result = listeOlustur(10, 20, 30, 'Merhaba')
print(result)

# 3- Göderilen 2 sayıyı arasındaki tüm asal sayıları bulun.
def asalBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1: 
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('İlk deger: '))
sayi2 = int(input('İkinci deger: '))
asalBul(sayi1, sayi2)

# 4- Kendisine gönderilen bir sayının tam bölenleini bir liste şeklinde döndürün
def bolenBul(deger):
    tamBolen = []
    for i in range(2, deger):
        if(deger % i == 0):
            tamBolen.append(i)
    return tamBolen

print(bolenBul(20))