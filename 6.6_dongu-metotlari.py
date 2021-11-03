import types

# RANGE
for item in range(50,100,20):
    # 50 den 100 e 20 şer olarak yazdırır.
    print(item)

print(list(range(5,100,10)))
# atadığımız degerleri liste içerisinde sakladık

#ENUMERATE
index = 0
text = 'deneme'
for x in text:
    print(f'index: {index} text: {x}')
    index += 1

# ya da
for item in enumerate(text):
    print(item)

# ya da
text2 = 'deneme2'
for index2, letter2 in enumerate(text2):
    print(f'index: {index2}, text: {letter2}')

#ZİP
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2, list3)))

# for ile yazdırmak isterrsek
for item2 in zip(list1, list2, list3):
    print(item2)