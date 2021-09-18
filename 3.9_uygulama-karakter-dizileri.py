website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

length = len(course)
length2= len(website)
str1= "abc"
str2 = "Hello world"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
print("1: ",length)
# 2- 'website' içinden www karakterlerini alın. 
print("2: ", website[7:10])
# 3- 'website' içinden com karakterlerini alın. 
print("3: ", website[length2-3:length2])
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın. 
print("4: ", course[0:15]+course[-15:])
# 5- 'course' ifadesindeki karakterleri tersten yazdırın. 
print("5: ", course[::-1])
#normalde 2 deseydik sıraya her 2 karakterden birini yazdıracaktı ama eksi ekleyince sonda atlayarak yazmaya başlar

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"


# 6- Yukarıda verilen değişkenler ile Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.
age = str(age)
print(f"6:  Benim adım {name} {surname} ,yaşım {32} mesleğim {job}")
# 7- 'Hello world' ifadesindeki w harfini W harfiyle değiştirin
# str2[6] = "W"
# print("7: ", str2) dersen hata alırsın :(
print("7: ", str2[0:6] + "W" + str2[7:11])
# 8- 'abc' ifadesini yan yana 3 kere yazdırın
print("8: ", str1*3)