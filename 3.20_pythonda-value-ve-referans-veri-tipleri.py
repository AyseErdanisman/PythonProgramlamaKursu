# value types => string, number

x = 5
y = 25

x = y

y = 10
# burada yapılan y deki değişiklik x i etkilemez
print(x, y)

# reference types => list
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b
b[0] = "grape"
# referance type olduğu için b üzerinde yapılan değişklik a yı da etkiledi

"""
bu iki örenk arasındaki temel fark işaret ettikleri adresler, value type da iki ayrı alan işaret edildiği için 
birinde yapılan değişiklik diğerini etkilemedi ama referance type da ikisi de aynı alanı işaret ettiği için 
birinde yapılan değişiklik diğerini de etkiledi (listeler adres bilgisi taşırken value tipler bir değer taşır)
"""
print(a, b)