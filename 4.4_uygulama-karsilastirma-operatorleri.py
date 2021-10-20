# 1- Girilen iki sayıdan hangisi büyüktür?
x = int(input('İlk sayı: '))
y = int(input('İkinci sayı: '))
result = x > y 
print(f'x:{x} y:{y} den büyüktür: {result}' )

# 2- Kullanıcıdan 2 vize (%60) ve final (%60) notunu alıp hesaplayınız. Eğer ortalama 50'nin üzerinde ise ekrana 
#    Geçti altında ise Kaldı yazdırın
v1 = int(input('İlk vize notu: '))
v2 = int(input('İkinci vize notu: '))
f = int(input('Final notu: '))
ort = (((v1 + v2) / 2) * 0.6) + (f * 0.4)
result2 = ort > 50
print(f'Ortamalnız: {ort} ve dersten geçme durumunuz: {ort>=50}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
a = int(input('Bir değer giriniz: '))
check2 = (a % 2 == 0)
print(f'Girilen sayı {a} ve çift olma durumu: {check2}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın
b = int(input('Bir değer giriniz: '))
check3 = (b > 0)
print(f'Sayı pozitif bir sayıdır: {check3}')

# 5- Parola ve e-mail bilgisini isteyip doğruluğunu kontrol edin.(email@sadikturan.com parola:123abc)
password = input('Password: ')
email = input('E-mail: ')
tpassword= '123abc'
temail = 'email@sadikturan.com'
checkpassword = (password == tpassword)
checkemail = (email == temail)

print(f'Girilen email bilgisi: {checkemail} ve Girilen şifre bilgisi: {checkpassword}')