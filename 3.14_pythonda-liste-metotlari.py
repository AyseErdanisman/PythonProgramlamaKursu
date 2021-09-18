numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
# numbers içerisindeki min degeri val değişkenine atadı - max da denebilir
vall = max(letters)
# alfabetik düzene göre atama yapar
valll = numbers[3:6]
# diyerek diziyi parçalayabiliriz
numbers[4] = 40
# dersek güncellenebilir bir liste olduğu için 4. indisteki 4 degeri yerine 40 degeri atanır

# liste üzerine bir eleman eklemek istersek
numbers.append(49)
# "" içerisinde ekleseydik string olarak ekleyecekti

numbers.insert(3, 74)
# insert sayesinde ekleme yapmak istediğimiz konumu seçebiliriz burada 3. indisin önüne 74 ü ekledik
numbers.insert(-1, 63)
# son indisin ÖNÜNE ekleme yaptı

numbers.pop()
# son eleman silebilmemizi sağladı, parantez içine hangi rakam yazılırsa o indisteki elemanı siler
numbers.remove(16)
# remove ise karakteri silmemizi sağlar, dizide 16 yı arara ve 16 nın bulunduğu indisi siler

numbers.sort()
# listeyi sıralı olarak düzenler
numbers.reverse()
# sort ile sırladıktan sonra listeyi tersine çevirmemizi sağladı
letters.sort()
letters.reverse()

print(val)
print(vall)
print(valll)
print(numbers)
print(letters)

print(numbers.count(10))
# numbers içerisinde kaç tane 10 olduğunu sayar
print(letters.count("a"))

numbers.clear()
# dizi elemanlarını temizledi
print(numbers)