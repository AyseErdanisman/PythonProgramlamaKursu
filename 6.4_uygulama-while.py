sayilar = [1, 3, 5 ,7 ,9, 12, 19, 21]

# 1- sayılar listesini while ile ekrana yazdırınız. 
i=0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
baslangic = int(input('Başlangıç değeri: '))
bitis = int(input('Bitiş değeri: '))

sayac = baslangic
while (sayac < bitis):
    if (sayac % 2 == 1):
        print(sayac)
    sayac += 1

# 3- 1 - 100 arasındaki sayıları azalan şeklinde yazdırın.
x = 100
while(x > 0):
    print(x)
    x -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []
y = 1
while (y <= 5):
    sayii = int(input(f'{y}. değeri giriniz: '))
    numbers.append(sayii)
    y += 1
numbers.sort()
print(numbers)

# 5- Kullanıcıdan aldığınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    * ürün sayısını kullanıcıya sorun
#    ** dictionary liste yapısı (name, price) şeklinde olsun
#    *** ürün ekleme işlemi bitiiğinde ürünleri ekranda while ile listeleyin 
urunler = []
adet = int(input('Girilecek ürün adeti: '))
a = 0
while(a < adet):
    name = input('Ürün ismi: ')
    price = float(input('Fiyat bilgisi: '))
    urunler.append({
        'name': name,
        'price': price
    })
    a += 1

for urun in urunler:
    print(f'Ürün adı: {urun["name"]} fiyat: {urun["price"]}')

