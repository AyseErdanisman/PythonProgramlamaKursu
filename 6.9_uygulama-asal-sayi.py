# Girilen bir sayının asal sayı olup olmadığını bulun

sayi = int(input('Sayı: '))
asalMi = True

if (sayi == 1):
    print('Girilen sayı asal sayı değildir')

for i in range(2, sayi):
    if (sayi % i == 0):
        asalMi = False
        break

if asalMi:
    print('Girilen sayi asaldır')
else:
    print('Girilen sayi asal değildir')