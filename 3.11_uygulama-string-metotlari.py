website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- " Hello word " karakter dizisinin baştaki ve sondaki boşluk karakterlerini silin
# result = " Hello word "
# result = result.strip()
# result = result.lstrip() --> left stript
# result = result.rstrip() --> right stript
# print(result)

#---------------------------------------------------------------------------------------------------

# 2- "www.sadikturan.com" ifadesi içerisindeki sadikturan bilgisi dışındaki her karakteri silin
# website = website.split(".")
# website[0] = ""
# website[2] = ""
# website = "".join(website)
# print(website)

# ya da 

# result = website.lstript(":/pth") da denebilir :)

#----------------------------------------------------------------------------------------------------

# 3- "course" karakter dizisinin tüm karakterini küçük harf yapın
# course = course.lower()
# print(course)
 
#----------------------------------------------------------------------------------------------------

# 4- "website" içerisinde kaç tane a karakteri vardır
# website = website.count('a')
# print(website)
# website = website.count('www', 0, 10) --> 0 ile 10. indis arasında www karaketrini arar

#----------------------------------------------------------------------------------------------------

# 5- "website" www ile başlayıp com ile bitiyor mu?
# isFound = website.startswith("www")
# isFounnd = website.endswith("com")
# print(isFound)
# print(isFounnd)

#-----------------------------------------------------------------------------------------------------

# 6- "website içerisinde ".com" ifadesi var mı?
# result = website.find(".com")
# print(result)
# result = website.rfind("Python") --> sağdan saymaya başlar

#-----------------------------------------------------------------------------------------------------

# 7- "course" içerisindeki karakterlerin hepsi alfabetik karakter mi? (isalpha, isdigit)
result = course.isalpha()
print(result)

#------------------------------------------------------------------------------------------------------

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * kaarakteri ekleyin
# result = "Contents"
# result = result.center(50, "*")
# result = result.ljust(50, "*") --> dersek ifadeyi sağa yaslayarak gerçekleştirir
# result = result.rjust(50, "*")
# print(result)

#-------------------------------------------------------------------------------------------------------

# 9- "course" karaker dizisindeki tüm boşluk karakterleini - karakteri ile değiştirin 
# course = course.replace(" ", "-")
# print(course)

#-------------------------------------------------------------------------------------------------------

# 10- "Hello World" karakter dizisinin "Word" ifadesini "There" olarak değiştirin
# result = "Hello World"
# result = result.replace("World", "There")
# print(result)

#-------------------------------------------------------------------------------------------------------

# 11- "course" karakter dizisini boşluk karakterlerinden ayırın
course = course.split(" ")
print(course)
