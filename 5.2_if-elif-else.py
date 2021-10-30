x = float(input('x: '))
y = float(input('y: '))

if x > y:
    print('x y den büyük')
elif x == y:
    print('x y ye eşit')
else: 
    print('y x den büyük')


sayi = int(input('Sayı: '))

if sayi > 0:
    print('Girilen deger pozitif')
elif sayi == 0:
    print('Girilen deger nötr')
else:
    print('Girilen deger negatif')