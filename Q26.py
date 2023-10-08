# Q26.write apython programme to convert the list of interger and integer of tuple to string usinfg lambda

list1 = [3, 34, 5, 46, 7, 68, 89, 79, 8, 9]
tup1 = (35, 46, 57, 6, 87, 9, 809, 9, 6, 45)
str1 = list(map(lambda x: str(x), list1))
str2 = list(map(lambda x: str(x), tup1))
print(str1)
print(str2)
