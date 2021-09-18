# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz. 
list1 = ["BMW", "Mercedes", "Opel", "Mazda"]

# 2- Liste kaç elemanlıdır?
print(len(list1))

# 3- Listenin ilk ve son elemanı nedir?
print(list1[0])
print(list1[3])

# 4- Mazda değerini Toyota ile değiştiriniz
list1[3] = "Toyota"
print(list1)

# 5- Mercedes listenin bir elemanı mıdır?
result = "Mercedes" in list1
print(result)

# 6- Listenin -2 indisindeki değer nedir?
print(list1[-2])

# 7- Listenin ilk 3 elemanını alın
print(list1[0:3])

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin 
list1[2] = "Toyota"
list1[3] = "Renault"
print(list1)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyiniz
list2 = ["Audi", "Nissan"]
list1 = list1 + list2
print(list1)

# 10- Listenin son elemanını silin
del list1[-1]
print(list1)
# 11- Liste elemanlarını tersten yazdırın
result = list1[::-1]
print(result)
# 12- Aşağıdaki verileri bir liste içinde saklayınız 

    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, 70, 60, 70]
studentB = ["Sena", "Turan", 1999, 80, 80, 70]
studentC = ["Ahmet", "Turan", 1998, 80, 70, 90] 

student = [studentA, studentB, studentC]
print(student)