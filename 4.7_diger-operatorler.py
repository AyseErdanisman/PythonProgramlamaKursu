# Indentity Operator: is

x = y = [1, 2, 3]
#  x ve y nı adres içerisinde tanımlanmış bir liste
z = [1, 2, 3]
# farklı adrese tanımlanmış liste

print(x == y)
print(x == z)
# her ikisi için de true degerini alırız çünkü denklik aranan koşul değişkenlere atanan değerlerin aynı olmasıdır

# ama biz referans degerindeki bir verinin adres kaşılaştırmasını yapmak istersek:
print(x is y)
print(x is z)
# adresler farklı olduğu için ilkinde true ikincisinde false degerini alırız 

a = [1, 2, 3]
b = [2, 4]
del a[2]
b[1] = 1
b.reverse() #listeyi tersine çevirir

print(a == b)
print(a is b)
print(a is not b)
# a b objesi değil midir??

# Membership Operator: in
l = ['apple', 'banana']
print('banaa' in l) #in ile aradığımız eleman liste içerisinde var mı diye soruyoruz
# banana bilgisis l içinde var mı??

name = 'Ayse'
print('y' in name)
print('A' not in name)