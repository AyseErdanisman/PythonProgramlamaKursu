fruits = {'orange', 'apple', 'banana'}
"""
    liste olduğu için fruits[0] diyip elemanlara ulaşamayız çünkü 
    liste dizi gibi indislenemez elemanlara ulaşmak için döngü kullanabiliriz
"""

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango", "grape", "apple"])
# apple zaten listede olduğu için tekrar eklenmez
fruits.remove('mango')
fruits.discard('apple')
print(fruits)
fruits.pop()
# normalde pop son elemanın silinmesini sağardı ama listede dizideki gibi sıralama olmadığı için
# rastgele bir eleman silinir, son elemanın silineceğinin garantisi yoktur
print(fruits)

myList = {1, 2, 5, 4, 4, 2, 1}
print(set(myList))
# set sayesinde tekrar eden elemanlar liste sadece 1 kere yazıldı
