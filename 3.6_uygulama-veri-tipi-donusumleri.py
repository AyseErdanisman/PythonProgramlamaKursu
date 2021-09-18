"""
    Daire Alanı = πr2
    Daire Çeversi = 2πr

    Yarıçapı verilen dairenin alanını ve çevresini hesaplayınız 
"""
radius = float(input("Yarıçapı giriniz: "))
pi = 3.14

circleArea = pi * (radius ** 2)
circleCir = 2 * pi * radius

print("Daire Alanı: ", circleArea)
print("Daire Çevresi: ", circleCir)

