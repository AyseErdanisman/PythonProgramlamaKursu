list = [1, 2, 3]
tuple = (1, "iki", 3)
# parantezsiz de tanımlanabilir ama okunabilirlik açısından () kullanmak yararlı

list[0] = "bir"
# tuple[0] = "bir"
# hata alırız çünkü tuple listeler değiştirilemez
names = ("demet", "emel", "ayşe") + tuple

print(list)
print(type(list))
print(tuple)
print(type(tuple))
print(names)