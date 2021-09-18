maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# DEGISKEN TANIMLAMA KURALLARI

#rakam ile baslayamaz

number1 = 10
print(number1)
number1 = 20
print(number1) 
#hata vermeden çalışır sadece ilk deger 10 iken sonradan 20 olarak atama yapılır

#turkce karakter kullanma

a = '10'
b = '20'
print(a+b) 
#string birleşitme yapıldığı için cevap 30 değil 1020 dir


x = 1
y = 4
name = 'yıldız'
ogrenci = True

#yukarıdaki ifadyi tek satırda tanımlamak için
x, y, name, ogrenci = (1, 2.3, 'cınar', False)