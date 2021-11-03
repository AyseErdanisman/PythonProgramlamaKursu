"""
1 - 100 arasında üretilecek bir sayıyı aşağı yukarı ifadeleri ile bulmaya çalışınız:
* 'random' modülü için rangom araştırması yapınız.
** 100 üzerinden puanlama yapınız. Her sor 20 puan olacaktır.
*** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın. 
"""

import random

sayi = random.randint(1, 10)
can = int(input('1 den 100 e kadar tutlan sayıyı tahmin etmek için kaç hak istersiniz? '))
hak = can
# can ı haka atamamızın sebebi puan hesaplamasında can değişkenini sabit tutumak ve kalan kısmı can üzerinden halletmek
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if(sayi == tahmin):
        print(f'Tebrikler {sayac}. hakkınızda bildiniz. Puanınız {100 - (100/can) * (sayac - 1)}')
        break
    elif(sayi > tahmin):
        print('Yukarı')
    else: 
        print('Aşağı')

    if (hak == 0):
        print(f'Hakkınız bitti. Doğru cevap: {sayi}')