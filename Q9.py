
# Q9: Write a Python program to arrange positive and negative numbers using lambda function
list1 = [-23, -102, -234, 54, 5, 3, 3, 23, 2, 4, 45, 4, 23]

list1.sort(key=lambda x: x)
print(list1)  # Output: [-234, -102, -23, 2, 3, 3, 4, 4, 5, 23, 23, 45, 54]
