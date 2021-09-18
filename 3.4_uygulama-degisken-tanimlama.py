"""
    1 - Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz 

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyadı
    Müşteri cinsiyet
    Müşteri tc kimlik 
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""

customerName = "Demet"
customerSurname = "Yılmaz"
customerNameSurname = customerName + ' ' + customerSurname
customerGender = True #Kadın
customerTC = '00000000000' #bu degeri herhangi bir hesaplamaya katmayacagimiz için string olarak tanımladık
customerYearOfBirth = 1985
customerAddress = "asdf"
customerAge = 2021 - customerYearOfBirth

print(customerNameSurname)

"""
    2- Asağidaki siparislerin toplam bilgisini hesaplayin

    Sparis 1 => 110 tl
    Sparis 2 => 1100.5 tl
    Sparis 3 => 356.95 tl 
"""

order1 = 110
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3
print("Total: ", total)
#, yerine + koyunca toplama yapmaya çalışıp hata veriyor virgülle yazdırman gerek