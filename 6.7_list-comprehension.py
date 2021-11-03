from typing import Text


for numbers in range(10):
    print(numbers)

# daha kolay olan yolu
numbers = [x for x in range(10)]
# 0 dan 10 a kadar olan sayıları for ile aldık ve x değişkenine atıp bir x değeri elde ediyoruz
print(numbers)

# ya da 
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

for x in range(10):
    print(x**2)

# ya da
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)

text = 'Hello'
list = []

# stringler için benzer bir şey yapmak istersek
for letter in text:
    list.append(letter)
print(list)

# ya da 
list = [letter for letter in text]
print(list)

years = [1994, 1993, 1987, 2000, 2003]
years = [2021-year for year in years]
print(years)

result = [x if x % 2 == 0 else 'TEK' for x in range(1, 10)]
print(result)

result2 = []

for x in range(3):
    for y in range(3):
        result2.append((x,y))
print(result2)

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)
