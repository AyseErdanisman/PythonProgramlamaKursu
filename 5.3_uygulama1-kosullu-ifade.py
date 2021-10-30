"""
1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyrt alabilme durumunu kontrol ediniz. Ehliyet
    alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalısır.
"""
isim = input('İsim: ')
yas = int(input('Yaş: '))
egitim = input('Eğitim durumu: ')

result = (yas >= 18) and ((egitim == 'lise') or (egitim == 'universite'))
if result:
    print(f'{isim} ehliyet başvurusu yapabilirsin')
else: 
    print(f'{isim} ehliyet başvurusu yapamazsın')

"""
2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamya göre not aralığına karşılık gelen not 
    bilgisini ekrana yazdırınız.
    0  - 24 => 0
    25 - 44 => 1
    45 - 54 => 2
    55 - 69 => 3
    70 - 84 => 4
    85 - 100 => 5
"""
yaz1 = float(input('1.Yazlın Notu: '))
yaz2 = float(input('2.Yazlın Notu: '))
soz = float(input('Sözlü Notu: '))

ort = (yaz1 + yaz2 + soz) / 3 

if ((ort >= 0) and (ort <= 25)):
    print('Not Bilgisi: 0')
elif((ort >= 25) and (ort < 45)):
    print('Not Bilgisi: 1')
elif((ort >= 45) and (ort < 55)):
    print('Not Bilgisi: 2')
elif((ort >= 55) and (ort < 70)):
    print('Not Bilgisi: 3')
elif((ort >= 70) and (ort < 85)):
    print('Not Bilgisi: 4')
elif((ort >= 85) and (ort <= 100)):
    print('Not Bilgisi: 5')
else:
    print('Geçerli deger giriniz')

"""
3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
    1. Bakım: 1. yıl
    2. Bakım: 2. yıl
    3. Bakım: 3. yıl
    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız 
    *** datetime modülünü kullanmanız gerekiyor
"""
import datetime

tarih = input('Aracın trafikğe çıktığı gün tarihi (2021/5/17)')
tarih  = tarih.split('/')

tcikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - tcikis
days = fark.days

if days <= 365:
    print('1. yıl')
elif days > 365 and days <= 365*2:
    print('2. yıl')
elif days > 365*2 and days <=365*3:
    print('3. yıl')
else:
    print('+3 yıl')