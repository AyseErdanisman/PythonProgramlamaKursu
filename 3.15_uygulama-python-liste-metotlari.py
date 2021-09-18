name = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1997]

# 1- "Cenk" ismini listenin sonuna ekleyiniz
name.append("Cenk")
print(name)

# 2- "Sena" değerini listenin başına ekleyiniz 
name.insert(0, "Sena")
print(name)

# 3- "Deniz" ismini listeden siliniz
# name.remove("Deniz")
# print(name)

# 4- "Deniz" isminin indeksi nedir
index = name.index ("Deniz")
print(index)

# 5- "Ali" listenin bir elemanı mıdır
result = "Ali" in name
print(result)

# 6- Liste elemanlarını ters çevirin
name.reverse()
print(name)

# 7- Liste elemanlarını alfabetik olarak sıralayınız
name.sort()
print(name)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız 
years.sort()
print(years)

# 9- str="Chevrolet, Dacia" karakter dizisini listeye çeviriniz
str="Chevrolet, Dacia"
result2 = str.split(",")
print(result2)

# 10- years dizisinin en büyük ve en küçük elemanı nedir
yrs = min(years)
yrss = max(years)
print(yrs, yrss)

# 11- years dizsinde kaç tane 1998 degeri vardır
print(years.count(1998))

# 12- years dizsinin tüm elemanlarını siliniz
years.clear()
print(years)

# 13- kullanıcıdan aldığınız 3 tane marka bilgisini bir listede saklayınız
st = input("İlk marka ismini yazın: ")
nd = input("İkinci marka ismini yazın: ")
rd = input("Üçüncü marka ismini yazın: ")

list= [st, nd, rd]
print(list)
