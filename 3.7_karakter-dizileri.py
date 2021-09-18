name = "Ayşe"
surname = "Erdanışman"
age = 21

greeting = "i'm " + name + " " + surname + " and \ni'm " + str(age) + " " + "years old"
print(greeting)
#\n alt satira geçmemizi sagladi

print(greeting[0])
#0. indisteki degeri verir
print(greeting[3])
print(greeting[7])

length = len(greeting)
#greeting ifadesinin uzunlugunu verir
print(greeting[length-1])
#0. indisten başlandığı için son indise length - 1 ifadesiyle ulaşabiliriz
# alternatif olarak print(greeting[-1]) ifadesini de kullanabiliriz.

print(greeting[2:7])
#2. indisten başla ve 7. ye kadar git
print()

print(greeting[7:])
#7. karakterden sona kadar alır
print()
print(greeting[:15])
#baştan başlayarak 15. karakterde durur
print()

print(greeting[2:40:2])
#2. indisten 40. indise 2 şer atlayarak yazar