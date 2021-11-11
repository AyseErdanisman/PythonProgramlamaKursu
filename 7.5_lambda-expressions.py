def square (num):
    return num **2 
numbers = [1, 3, 5, 7, 9]
result = list(map(square, numbers))
print(result)

for item in list(map(square, numbers)):
    print(item)