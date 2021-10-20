x = 6
hak = 5
devam = 'e'
result = 5 < x < 6 

# and 
result2 = (x > 5) and (x < 10)
# koşulun her iki durumu da doğru olursa ture değerini döndürür
print(result2)
result3 = (hak > 0) and (devam == 'e')
print(result3)

# or
result4 = (x > 0) or (x % 2 == 0)
# true deger için ifadelerden sadece birinin true olması yeterli
print(result4)

# not
result5 = not(x > 0)
# sourlan sorunun cevabının tam tersini üretir

# x, 5-10 arasında olan bir çift sayı mı??
result5 = ((x > 5) and (x < 10) and (x % 2 == 0))
print(result5)