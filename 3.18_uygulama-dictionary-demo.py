"""
    ogrenciler ={
        "120": {
            "ad": "Ali",
            "soyad": "Yılmaz", 
            "telefon": "1231 231 23 12"
        },

        "125": {
            "ad": "Can",
            "soyad": "Korkmaz",
            "telefon": "1231 123 12 12"
        },

        "128": {
            "ad": "Volkan",
            "soyad": "Yükselen",
            "telefon": "1231 123 12 12"
        }
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız 
       bilgilerle dictionary içinde saklayınız.

    2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini görseriniz 
"""

ogrenciler = {

}

number = input("ogrenci no: ")
name = input("ogrenci ad: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon no: ")

"""
    ogrenciler[number] = {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
    burada yapılanlar update metoduyla da yapılabilir
"""

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

number = input("ogrenci no: ")
name = input("ogrenci ad: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon no: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

number = input("ogrenci no: ")
name = input("ogrenci ad: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon no: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print("*"*50)

# 2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini görseriniz 
ogrNo = input("ogrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(f'Aradığınız {ogrNo} numaralı öğrencinin adı: {ogrenci["ad"]} soyadı: {ogrenci["soyad"]} ve telefonu ise {ogrenci["telefon"]} dir')