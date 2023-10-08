
# Q8: Write a program to find the intersection of two lists using lambda functions
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [10, 20, 30, 40, 50, 60, 70, 8, 9]

list3 = list(filter(lambda x: x in list1, list2))
print(list3)  # Output: [8, 9]
