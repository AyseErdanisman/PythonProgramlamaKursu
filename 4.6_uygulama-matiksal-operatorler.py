# 1- Girilen bir sayı 0 - 100 arasnıda olup olmadığını kontrol edin.ü
from types import resolve_bases


sayi = input("Sayı Girişi: ")
result = (int(sayi) > 0) and (int(sayi) < 100)
print(f"Sayı 0 ile 100 arasındadır: {result}")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi2 = input('Sayı Girişi: ')
result2 = (int(sayi2) > 0) and (int(sayi) % 2 == 0)
print(f'Girilen sayı pozitif ve çift sayıdır: {result2}')

# 3- E-mail ve parola bilgileri ile giriş kontrolü yapınız 
email = 'email@ayseerdanisman'
password = 'abc123'

inputsemail = input('Email: ')
inputpassord = input('Password: ')

result3 = ((email == inputsemail) and (password == inputpassord))
print(f'Giris {result3}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

sirala = (a > b) and (a > c) 
print(f'a en büyük sayıdır: {sirala}')

sirala = (b > a) and (b > c)
print(f'b en büyük sayıdır: {sirala}')

sirala = (c > a) and (c > b)
print(f'c en büyük sayıdır: {sirala}')

# 5- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayınız 
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın. 
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalı.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın 

vize1 = int(input('İlk vize: '))
vize2 = int(input('İkinci vize:'))
final = int(input('Final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
result4 = (final >= 70) or ((ortalama >= 50) and (final >= 50))
#result4 = (ortalama >= 50) and (final >= 70) 
print(result4)

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir??
#    0    - 18.4 => Zayıf
#    18.5 - 24.9 => Normal
#    25.0 - 29.9 => Fazla Kilolu
#    30.0 - 34.9 => Obez

isim = input('İsim: ')
kilo = float(input('Kilo: '))
boy = float(input('Boy: '))

vke = (kilo) / (boy ** 2)

print(f'Adınız: {isim}')
print('Kilo: ', kilo)
print('Boy: ', boy)

result5 = (vke > 0) and (vke <= 18.4)
print(f'Zayıf: {result5}')

result5 = (vke >= 18.5) and (vke <= 24.9)
print(f'Normal: {result5}')

result5 = (vke >= 25.0) and (vke <= 29.9)
print(f'Fazla Kilolu: {result5}')

result5 = (vke >= 30.9) and (vke <= 34.9)
print(f'Obez: {result5}')