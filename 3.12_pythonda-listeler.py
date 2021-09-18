# l = [1, 2, 3]
# l = ["bir", 2, True, 5.6]
# print(l)

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]

numbers  = list1 + list2
print(numbers)

userA = ["Nehir", 24]
userB = ["Aslı", 17]

# users = userA + userB
# dersek listeleri birleştiri ama biz dizi içinde dizi saklamak istersek 

users = [userA, userB]
# # birinci indis ["Nehir", 24], ikinci indis ["Aslı", 17] oldu
# print(users)

# eğer isimlere ulaşmak istersek
print(users[1][0])