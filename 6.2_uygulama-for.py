sayilar = [1, 3, 5, 7, 9 ,12, 19, 21]

# 1- Sayilar listesindeki hangi sayılar 3 ün katıdır?
for a in sayilar:
    if (a % 3 == 0):
        print(a)
print('----------------------------------------------------')

# 2- Sayılar listesinde sayıların toplamı kaçtır?
topla = 0
for b in sayilar:
    topla = topla + b
print(topla)
print('----------------------------------------------------')

# 3- Sayılar listesindeki tek sayıların karesini alınız 
for c in sayilar:
    if (c % 2 == 1): 
        kare = c ** 2
    print(kare)    
print('----------------------------------------------------')

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
for d in sehirler:
    if (len(d) <= 5):
        print(d)
print('----------------------------------------------------')

urunler = [
    {'name':'samsung S6', 'price': '3000'},
    {'name':'samsung S7', 'price': '4000'},
    {'name':'samsung S8', 'price': '5000'},
    {'name':'samsung S9', 'price': '6000'},
    {'name':'samsung S10', 'price': '7000'}
]

# 5- Ürünlerin toplam fiyatı nedir?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)
print('----------------------------------------------------')

# 6- Ürünlerden fiyatı en az 5000 olan ürünleri gösteriniz
for urun2 in urunler:
    if ((int(urun2['price']) >= 5000)):
        print(urun2['name'])