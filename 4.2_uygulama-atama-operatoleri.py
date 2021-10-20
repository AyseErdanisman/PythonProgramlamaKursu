x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z nin toplamı kaçtır?
a  = input("ilk degeri giriniz: ")
b =  input("ikinci degeri giriniz: ")
c = int(a) * int(b) + (x+y+z)
print(c)

# 2- y'nin x'e kalansız bölümünü hesaplayınız
print(y // x)

# 3- (x,y,z) toplamının mod 3 ü nedir
print((x + y + z) % 3)

# 4- y'nin x. kuvvetini hesaplayınız
print(y**x)

# 5- x, *y, z = numbers işlemine göre z nin küpü kaçtır?
x, *y, z = numbers
#burada x 1. elemanı alır, z sonuncu elemanı alır, y ise ortada kalan tüm elemanları alır
print(y) #[5, 7, 10]
print(z ** 3)

# 6- x, *y, z = numbers işlemine göre y'nin degerleri toplamı kaçtır?
x, *y, z = numbers
result = y[0] + y[1] + y[2]
print(result)
