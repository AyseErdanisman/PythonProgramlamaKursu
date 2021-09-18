x = input("1.sayi: ")
#kullanicidan deger almak icin input komutunu kullandik

y = input("2.sayi: ")
toplam = int(x) + int(y)

print(toplam)
"""
    inputtan gelen deger string türünde oldugundan x=10 y=20 icin konusursak cikti 1020 olur cunku toplam = x + y dedik
    bunun yasanmamasi icin toplam = int(x) + int1(y) dememiz gerek
"""
#secilen tum satirlari yorum satiri yapmak icin kisa yol = ctrl + K + C

a = 10
b = 2.5
name = "Cınar"
isOnline = True

# print(type(a))
# print(type(b))
# print(type(name))
# print(type(isOnline))

#Type Conversion

#int to float
a = float(a)
print(a)
print(type(a))

#float to int
b = int(b)
#2.5 in ondalıklı kısmı gider ve sadece 2 kalır
print(b)
print(type(b))

result = a + b
print(result)
print(type(result))

result2 = str(a) + str(b)
print(result2)
print(type(result2))

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

#bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))