# Q25.write a python program to add 2 list and calculate difference between them

list1 = [1, 23, 54, 567, 7, 6]
list2 = [4, 345, 46, 756, 68, 6789]
sum1 = list(map(lambda a, b: a+b, list1, list2))
diff = list(map(lambda a, b: a-b, list1, list2))
print(sum1)
print(diff)
