def changeName(n):
    n = 'Ada'

name = 'Aslı'
changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'

sehirler = ['Ankara', 'İzmir']
n = sehirler[:] #slicing - şehirler dizisindeki tüm elemanları n ismindeki diziye aktardık([0:2] şeklide de atama yapılabilir)
# normalde istanbul güncellemsi n listesinde de gözükmeliydi ama : yüzünden yukarıdaki gibi değişken kopyası oluşturuldu
change(sehirler[:])
# n parametresine sehirler dizisinin adersi gönderilir ve ilk indisteki Ankara ifadesi İstanbulla değiştririlir
# yukarıdaki changeName deki gibi değişkenin bir kopyası oluşturulmaz, sadece adres kopyalaması yapılır
print(sehirler)
print(n)
# slicingi n ile yapmak yerine change(sehirler[:]) \n print(sehirler) ifadesini yazarak da yapabiliriz

def add(*params):
    # paremetre sayısınını kaç değer girilecekse ona göre belirledik
    print(params)
    return sum((params))

print(add(10, 20, 50, 10, 4))

# eğer sum fonksiyonunu kullanmak istemezsek
def add(*params):
    print(type(params))
    sum = 0

    for n in params:
        sum = sum + n
    
    return sum
print(add(10, 10, 10))

def displayUser(**args):
    # tuple listesi değil dictionary olmasını istediğimiz için ** kullandık
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

displayUser(name = 'Deniz', age = 8, city = 'Mugla')
displayUser(name = 'Melis', age = 12, city = 'Trabzon', phone = '12312312')
displayUser(name = 'Asya', age = 10, city = 'Antalya', phone = '14714714', email = 'asya@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value 2')