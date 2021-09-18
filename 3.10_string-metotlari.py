message = "Hello there. My name is Ayse Erdanisman "
# message = message.upper() 
# tüm harfler büyük olur

# message = message.lower()
# tüm harfler küçük olur

# message = message.title()
# cümledeki her kelime büyük hafle başlar

# message = message.capitalize()
# verilen cümlede sadece en baştaki harf büyük yazılır

# message = message.strip()
# cümle başındaki ve sonundaki boşuk karakterini siler

# message = message.split()
# her bir boşuk karaketine göre karakter dizisini böler
# ['Hello', 'there.', 'My', 'name', 'is', 'Ayse', 'Erdanisman'] gibi
# print(message[0])  dersek H değil Hello ifadesi karşımıza gelir
# message = message.split(".") dersek de . lar arasında bölünme gerçekleşir

#-----------------------------------------------------------------------------------------

# message = message.split()
# karakter dizisini önce boşluklardan parçalayalım
# ayrılmış elemanları birleştrimek istersek de:
# message = " ".join(message)
# boşluk yerine --- koysaydık ayırdığı elemanlar arasına boşluk yerine --- eklerdi 

#-------------------------------------------------------------------------------------------

# index = message.find("Ayse")
# burada message içinde Ayse kelimesini aradı ve bulduğu ilk indis numarasını index değişkenine atadı
# Eğer cümle içerisinde bulunmayan bir kelime aratırsak da -1 degerini döndürü
# isFonud = message.startswith("H")# ya da endwith("H")
# cümle H ile mi başlıyor/bitiyor onu belirtir
# print(isFonud) 
# print(index)

#--------------------------------------------------------------------------------------------

# message = message.replace("Erdanisman","ERDANISMAN")
# bu metot cümle içerisinde Erdanisman kelimesini arar eğer varsa ERDANISMAN olarak değiştiri
# bunu url oluştururken türkçe karakterleri değiştimek için kullanabilirsin
# message = message.replace("ç","c").replace("ı","i").replace(" ","-")

#--------------------------------------------------------------------------------------------

# message = message.center(100)
# 100 karakterlik bir container oluşturarak cümleyi ortaya yerleştirir
# message = message.center(50,"*")
print(message) 

