name = 'Ayse Erdanisman'

for letter in name:
    if (letter == 'a'):
        # break dersek a dan sonrası ekrana yazılmaz ve döngü durur
        continue # dersek a harflerini atlayarak yazmaya devam eder
    print(letter)

x = 0
while (x < 5):
    x += 1
    if(x == 2):
        continue
    print(x)

# 1 den 100 e kadar olan tek sayıların toplamı
toplam = 0
sayac = 0
while (sayac <= 100):
    sayac += 1
    if(sayac % 2 == 0):
        continue
    toplam = toplam + sayac
print(toplam)