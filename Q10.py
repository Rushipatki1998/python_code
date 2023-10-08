
# Q10: Write a Python program to calculate even and odd numbers in an array using lambda function
list1 = [232, 32, 323, 23, 23, 24, 4, 5, 65, 7, 678, 789, 42, 3, 2]

even_list = list(filter(lambda x: x % 2 == 0, list1))
odd_list = list(filter(lambda x: x % 2 != 0, list1))

print(even_list)  # Output: [232, 32, 24, 4, 678, 42, 2]
print(odd_list)   # Output: [323, 23, 23, 5, 65, 7, 789, 3]
