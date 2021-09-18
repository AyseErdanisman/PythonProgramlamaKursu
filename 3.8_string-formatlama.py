name = "Ayşe"
surname = "Erdanışman"
age = 21

print("Ben {} {}".format(name, surname))
#aralara boşluk bırakmakla uğraşmadan bizim için halletti
#0. indise Ayşe 1. indise ise Erdanışmanı yerleştirdi

#print("Ben {1} {0}".format(name, surname)) yaparak indisleri düzenleyebilirsin
#print("Ben {n} {s}".format(n=name, s=surname))
print("Ben {} {} ve {} yaşındayım".format(name, surname, "21"))

random = 200/700
print("random: {r:1.3}".format(r=random))
#{r:1.3} => 1 - tam kısım için kaç karakterlik boşluk bırakılacağını ifade eder
#           3 - virgülden sonra kaç rakamın alınacağını gösterir

print(f"Ben {name} {surname} ve {age} yaşındayım")
#bu da kullaılabilir

