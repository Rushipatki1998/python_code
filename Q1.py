
# Q1: Write the program to sort a list using lambda function
list1 = [45, 543, 534, 50, 34, 45, 34, 5]

# Sorting the list
list1.sort(key=lambda x: x)
print(list1)  # Output: [5, 34, 34, 45, 45, 50, 534, 543]

list1 = [(432, 423), (54, 5), (4, 5, 234)]
list1.sort(key=lambda x: x)
print(list1)  # Output: [(4, 5, 234), (54, 5), (432, 423)]
