def say(name = 'user'):
    # Eğer kullanıcı herhangi bir isim girmezse default olarak user yazacak
    return 'Hello ' + name

name = say('Ayse')
print(name)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla (dogumYili):
    return 2021 - dogumYili

ageSimay = yasHesapla(2007)
ageSelim = yasHesapla(1998)
ageAyse = yasHesapla(2000)

def emeklilik(dogumYili, isim):
    
    """
        DOCSTRING: Emeklilige kac yil kaldigini hesaplar,
        INPUT: dogumYili
        OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 60 - yas

    if(emeklilik > 0):
        print(f'Emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Emekliliğiniz dolmuştur')

emeklilik(1988, 'Ahmet')

print(help(emeklilik))
print(help(list.append))