# Q22.write a programme for addiction of 3 list

list1 = [1, 23, 4]
list2 = [1, 2, 5]
list3 = [6, 7, 8, 9]
result = list(map(lambda a, b, c: a+b+c, list1, list2, list3))
print(result)
